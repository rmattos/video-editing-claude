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

1. Baixe as imagens dos apps, uma vez: `node baixar-assets.mjs` (Node 18 ou mais novo, sem instalar nada). Ele baixa o ícone e 5 prints do Duolingo, do Spotify e do iFood, e o ícone do Nubank, direto da App Store do Brasil.
2. Crie o projeto e instale os fluxos:
   `npx hyperframes init meu-video --resolution portrait` (use `landscape` nas pastas 03 e 04, `square` na 02)
   `npx skills add heygen-com/hyperframes --full-depth`
3. Copie o CONTEÚDO da pasta do exemplo (assets, audio, fotos, cenas, dados.json, roteiro.txt) para dentro do projeto.
4. Abra o Claude Code na pasta do projeto e cole o texto de `prompt.md`.

Cada exemplo também tem `prompt-detalhado.md`: a mesma encomenda com mais regras, para quem quer controlar cada cena.

## O que é real e o que é do kit

- Apps (Duolingo, Spotify, iFood, Nubank): nomes, notas e contagens de avaliação vêm da App Store do Brasil, consultada em 28/09/2026. Ícones e prints são material público da loja e pertencem aos donos. O prompt pede o selo "Demonstração não oficial". Não sugira parceria e confira os termos antes de publicar algo comercial.
- Os prints mudam quando o app atualiza a loja. O mapa "print-N mostra tal coisa" vale para 28/09/2026: abra os arquivos baixados e ajuste o prompt se a ordem mudou.
- Café Serra é uma marca fictícia. As seis imagens são ilustrações vetoriais criadas para o exemplo, não fotos. Troque pelas suas mantendo os nomes.
- A fábula "A cigarra e a formiga" é de Esopo (domínio público); o texto de `roteiro.txt` é uma recontagem.
- As quatro trilhas são originais, sintetizadas para o kit, sem direitos de terceiros. O código que gerou imagens e música está em `_fontes`.
- `dados.json`: avaliações totais da loja BR (todas as versões) e nota média. Os números mudam com o tempo.

## O que foi testado

- `baixar-assets.mjs`: testado contra um servidor local que imita a API da Apple (baixa, trata falha e usa o plano B de `assets.json`). Os endereços da API e das imagens foram abertos e conferidos no navegador, mas o download real das imagens não pôde ser rodado no ambiente onde o kit foi montado. Se algo falhar, a mensagem diz qual arquivo.
- Narração: `hyperframes tts --lang pt-br --voice pf_dora` gerou todas as falas; as durações medidas cabem nas cenas. A qualidade da voz precisa ser ouvida por você.
- `hyperframes beats` rodou na trilha do café: o detector marca o dobro do andamento real (184 em vez de 92), por isso o prompt pede um corte a cada 4 marcações.
- `amostras/`: vídeos montados à mão com os mesmos arquivos, para mostrar o resultado esperado. Não são a saída dos fluxos oficiais do Hyperframes; o que o Claude gerar a partir do prompt vai diferir.
  - `exemplo-app-foco.mp4`: app fictício, narração e trilha.
  - `cafe-serra-amostra.mp4`: cortes nas batidas reais da trilha.
  - `cigarra-formiga-amostra.mp4`: fábula completa com voz, legendas e trilha.
- Não há amostra dos exemplos 01 e 03: eles dependem dos ícones e prints baixados, que não pude baixar aqui.
