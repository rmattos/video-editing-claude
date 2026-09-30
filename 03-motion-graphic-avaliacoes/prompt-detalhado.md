/motion-graphics

Crie um motion graphic de 8 segundos, 1920x1080, com fundo escuro (#0b1220), em português do Brasil: um gráfico de barras horizontais animado com dados REAIS lidos do arquivo dados.json. Leia o arquivo; não invente nem arredonde valores por conta própria.

REGRAS
- Não baixe nada da internet: use somente os arquivos listados abaixo.
- Sem emoji. Fonte sem serifa que já exista no computador (Arial ou Segoe UI).
- Composição determinística: sem Date.now(), sem Math.random(), sem fetch de rede. A contagem dos números é uma animação do GSAP.

ARQUIVOS (já estão na pasta do projeto)
- dados.json: 4 apps com "avaliacoes" e "nota" na App Store do Brasil, consultados em 28/09/2026
- assets/icone-spotify.jpg, assets/icone-ifood.jpg, assets/icone-nubank.jpg, assets/icone-duolingo.jpg: ícones 1024x1024; mostre em 96x96 com cantos arredondados
- audio/trilha-motion.mp3: trilha de 8 s, 120 bpm

ROTEIRO POR TEMPO
- 0,0 a 0,8 s: título "Avaliações na App Store do Brasil" entra por máscara; subtítulo "4 apps, lado a lado".
- 0,8 a 2,0 s: as 4 linhas aparecem em sequência (0,15 s entre elas), com ícone e nome, e a barra ainda vazia.
- 2,0 a 6,0 s: as barras crescem com ease power3.out. O comprimento é proporcional a "avaliacoes" (Spotify = 100%). O número ao lado conta de 0 até o valor, no formato "11,1 mi", "8,9 mi", "1,6 mi", "1,1 mi".
- 6,0 a 7,2 s: a barra do Spotify pulsa e aparece "Spotify tem quase 10 vezes as avaliações do Duolingo".
- 7,2 a 8,0 s: rodapé "Fonte: App Store (BR), 28/09/2026" aparece; no fim, tudo sai com fade.

ÁUDIO
Trilha com volume 0,7, fade-out de 0,6 s no final.

ENTREGA
1. Rode `npx hyperframes check` e corrija até não haver erros.
2. Renderize: `npx hyperframes render --format mp4 -o renders/avaliacoes.mp4`.
3. Tire 3 quadros (início, meio e fim) com `npx hyperframes snapshot` e me diga o que ficou diferente do combinado.
