#!/usr/bin/env node
// baixar-assets.mjs — baixa ícones e prints públicos da App Store do Brasil para os exemplos.
// Uso:  node baixar-assets.mjs            (baixa tudo, ~15 arquivos)
//       node baixar-assets.mjs duolingo   (só um app)
// Requer Node 18+ (fetch nativo). Não instala nada e não envia dados seus a lugar nenhum.
import { mkdir, writeFile, readFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const AQUI = dirname(fileURLToPath(import.meta.url));
const API = process.env.ITUNES_API || "https://itunes.apple.com";
const UA = "Mozilla/5.0 (compatible; exemplos-hyperframes/1.0)";

// slug -> onde salvar ícone + prints, e onde copiar o ícone para o motion graphic
const ALVOS = {
  duolingo: { pasta: "01-app-duolingo/assets/duolingo", prints: 5 },
  spotify:  { pasta: "01b-app-spotify/assets/spotify",  prints: 5 },
  ifood:    { pasta: "01c-app-ifood/assets/ifood",      prints: 5 },
  nubank:   { pasta: null, prints: 0 },
};
const PASTA_ICONES = "03-motion-graphic-avaliacoes/assets";

const fallback = JSON.parse(await readFile(join(AQUI, "assets.json"), "utf8")).apps;
const so = process.argv[2];
const slugs = so ? [so] : Object.keys(ALVOS);
if (so && !ALVOS[so]) { console.error(`App desconhecido: ${so}. Use: ${Object.keys(ALVOS).join(", ")}`); process.exit(1); }

const tamanho = (url, t) => url.replace(/\/\d+x\d+bb\.(jpg|png|webp)$/i, `/${t}bb.jpg`);
const esperar = (ms) => new Promise((r) => setTimeout(r, ms));

async function lookup(id) {
  const r = await fetch(`${API}/lookup?id=${id}&country=br`, { headers: { "User-Agent": UA } });
  if (!r.ok) throw new Error(`lookup HTTP ${r.status}`);
  const j = await r.json();
  const a = j.results?.[0];
  if (!a) throw new Error("app não encontrado");
  return {
    nome: a.trackName, vendedor: a.sellerName, nota: a.averageUserRating, avaliacoes: a.userRatingCount,
    loja: (a.trackViewUrl || "").split("?")[0],
    icone: tamanho(a.artworkUrl512, "1024x1024"),
    prints: (a.screenshotUrls || []).map((u) => tamanho(u, "1242x2688")),
  };
}

async function baixar(url, destino) {
  for (let tentativa = 1; tentativa <= 3; tentativa++) {
    try {
      const r = await fetch(url, { headers: { "User-Agent": UA } });
      const tipo = r.headers.get("content-type") || "";
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      if (!tipo.startsWith("image/")) throw new Error(`não é imagem (${tipo})`);
      const buf = Buffer.from(await r.arrayBuffer());
      if (buf.length < 2000) throw new Error(`arquivo pequeno demais (${buf.length} bytes)`);
      await mkdir(dirname(destino), { recursive: true });
      await writeFile(destino, buf);
      return buf.length;
    } catch (e) {
      if (tentativa === 3) throw e;
      await esperar(600 * tentativa);
    }
  }
}

const creditos = [];
let falhas = 0;
for (const slug of slugs) {
  const alvo = ALVOS[slug];
  let dados, origem = "API iTunes Lookup";
  try { dados = await lookup(fallback[slug].id); }
  catch (e) { console.warn(`[${slug}] lookup falhou (${e.message}); usando URLs salvas em assets.json`); dados = fallback[slug]; origem = "assets.json"; }

  const itens = [];
  if (alvo.pasta) itens.push([dados.icone, join(AQUI, alvo.pasta, "icone.jpg")]);
  itens.push([dados.icone, join(AQUI, PASTA_ICONES, `icone-${slug}.jpg`)]);
  if (alvo.pasta) dados.prints.slice(0, alvo.prints).forEach((u, i) => itens.push([u, join(AQUI, alvo.pasta, `print-${i + 1}.jpg`)]));

  for (const [url, destino] of itens) {
    try {
      const n = await baixar(url, destino);
      console.log(`ok   ${destino.replace(AQUI, ".")}  (${Math.round(n / 1024)} KB)`);
      creditos.push({ app: slug, arquivo: destino.replace(AQUI, "."), origem: url });
    } catch (e) { falhas++; console.error(`FALHOU ${destino.replace(AQUI, ".")}: ${e.message}`); }
  }
  creditos.push({ app: slug, nome: dados.nome, vendedor: dados.vendedor, loja: dados.loja, fonte: origem });
  await esperar(300);
}

await writeFile(join(AQUI, "assets-baixados.json"),
  JSON.stringify({ baixado_em: new Date().toISOString(), aviso: "Marcas, ícones e prints pertencem aos respectivos donos. Uso como demonstração, sem indicar parceria.", itens: creditos }, null, 2));
console.log(falhas ? `\nTerminou com ${falhas} falha(s). Rode de novo ou veja a mensagem acima.` : "\nTudo baixado. Crédito e origem de cada arquivo em assets-baixados.json");
process.exit(falhas ? 1 : 0);
