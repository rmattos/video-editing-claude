# Kit de exemplos: vídeos com Claude Code + Hyperframes

Cada pasta numerada é um exemplo pronto: um `prompt.md` real e os arquivos que ele usa.

| Pasta | Fluxo | Formato | O que é |
|---|---|---|---|
| `01-app-duolingo` | `/product-launch-video` | 1080x1920, 25 s | app famoso, com ícone e prints reais da App Store |
| `01b-app-spotify`, `01c-app-ifood` | `/product-launch-video` | 1080x1920, 25 s | o mesmo prompt para outros dois apps |
| `02-produto-cafe-serra` | `/music-to-video` | 1080x1080, 15 s | seis fotos cortadas no ritmo da música |
| `03-motion-graphic-avaliacoes` | `/motion-graphics` | 1920x1080, 8 s | barras animadas com dado real |
| `04-storytelling-cigarra-formiga` | `/faceless-explainer` | 1920x1080, 50 s | fábula narrada em português |

## Como usar

### Instalar (uma vez)

Precisa de Git, Node 22 ou mais novo, FFmpeg e Claude Code.

```
git clone https://github.com/rmattos/video-editing-claude
cd video-editing-claude
node baixar-assets.mjs
npx skills add heygen-com/hyperframes --full-depth -g -y -a claude-code
npx hyperframes doctor
```

- `node baixar-assets.mjs` baixa da App Store do Brasil o ícone e 5 prints do Duolingo, do Spotify e do iFood, mais o ícone do Nubank. Roda com Node 18 ou mais novo, sem instalar nada.
- `npx skills add ... -g -y -a claude-code` instala as 28 skills do Hyperframes no seu Claude Code (`~/.claude/skills`), sem perguntas. Basta rodar uma vez, não precisa repetir a cada projeto.
- `npx hyperframes doctor` mostra o que falta (Node, FFmpeg, Chrome).

### Rodar um exemplo

1. Crie uma pasta nova para o vídeo. Troque o nome a cada exemplo, porque o `init` recusa pasta que não está vazia:
   `npx hyperframes init video-duolingo --resolution portrait`
   Formato de cada pasta: `portrait` em 01, 01b e 01c; `square` em 02; `landscape` em 03 e 04.
2. Copie o CONTEÚDO da pasta do exemplo (assets, audio, fotos, cenas, dados.json, roteiro.txt) para dentro do projeto. Pode arrastar no Explorer/Finder ou usar:
   `cp -r 01-app-duolingo/. video-duolingo/`
3. Entre na pasta e abra uma **sessão nova** do Claude Code, para as skills carregarem:
   `cd video-duolingo` e depois `claude`
4. Cole o texto de `prompt.md`. Quando o Claude terminar, confira e renderize:
   `npm run check` e `npm run render`

Cada exemplo também tem `prompt-detalhado.md`: a mesma encomenda com mais regras, para quem quer controlar cada cena.

## O que é real e o que é do kit

- Apps (Duolingo, Spotify, iFood, Nubank): nomes, notas e contagens de avaliação vêm da App Store do Brasil, consultada em 28/09/2026. Ícones e prints são material público da loja e pertencem aos donos. O prompt pede o selo "Demonstração não oficial". Não sugira parceria e confira os termos antes de publicar algo comercial.
- Os prints mudam quando o app atualiza a loja. O mapa "print-N mostra tal coisa" vale para 28/09/2026: abra os arquivos baixados e ajuste o prompt se a ordem mudou.
- Café Serra é uma marca fictícia. As seis imagens são ilustrações vetoriais criadas para o exemplo, não fotos. Troque pelas suas mantendo os nomes.
- A fábula "A cigarra e a formiga" é de Esopo (domínio público); o texto de `roteiro.txt` é uma recontagem.
- As quatro trilhas são originais, sintetizadas para o kit, sem direitos de terceiros. O código que gerou imagens e música está em `_fontes`.
- `dados.json`: avaliações totais da loja BR (todas as versões) e nota média. Os números mudam com o tempo.

## O que foi testado

- Instalação: `npx hyperframes init` e `npx skills add heygen-com/hyperframes --full-depth -g -y -a claude-code` foram rodados no Linux (CLI 0.8.96) e instalaram as skills sem perguntas. No Windows não foi testado.
- `baixar-assets.mjs`: testado contra um servidor local que imita a API da Apple (baixa, trata falha e usa o plano B de `assets.json`). Os endereços da API e das imagens foram abertos e conferidos no navegador, mas o download real das imagens não pôde ser rodado no ambiente onde o kit foi montado. Se algo falhar, a mensagem diz qual arquivo.
- Narração: `hyperframes tts --lang pt-br --voice pf_dora` gerou todas as falas; as durações medidas cabem nas cenas. A qualidade da voz precisa ser ouvida por você.
- `hyperframes beats` rodou na trilha do café: o detector marca o dobro do andamento real (184 em vez de 92), por isso o prompt pede um corte a cada 4 marcações.
