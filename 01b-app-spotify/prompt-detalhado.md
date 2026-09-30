/product-launch-video

Crie um vídeo promocional vertical (1080x1920) de 25 segundos do app Spotify, para Reels, Shorts e TikTok. É uma demonstração NÃO oficial feita com o material público da loja de apps.

REGRAS
- Não rode `hyperframes capture` e não baixe nada da internet: use somente os arquivos listados abaixo, que já estão na pasta do projeto.
- Todo texto na tela e toda a narração em português do Brasil. Sem emoji.
- Sem rosto, pessoa ou cena filmada: só o ícone, os prints e elementos gráficos feitos em HTML, CSS e GSAP.
- Fonte sem serifa que já exista no computador (Arial ou Segoe UI); não carregue fonte da internet.
- Composição determinística: sem Date.now(), sem Math.random(), sem fetch de rede.
- Selo pequeno no canto superior durante o vídeo inteiro: "Demonstração não oficial · sem vínculo com Spotify".

ARQUIVOS (já estão na pasta do projeto)
- assets/spotify/icone.jpg: ícone do app, 1024x1024
- assets/spotify/print-1.jpg: músicas e podcasts em um só lugar
- assets/spotify/print-2.jpg: podcasts
- assets/spotify/print-3.jpg: letra das músicas na tela
- assets/spotify/print-4.jpg: playlists selecionadas para você
- assets/spotify/print-5.jpg: playlist compartilhada com amigos
- audio/trilha-app.mp3: trilha de fundo, 112 bpm, 28 s
Cada print é um retrato com texto e fundo colorido próprios da loja. Mostre inteiro (object-fit: contain) dentro de uma moldura de celular desenhada em CSS; não corte, não distorça e não repita na legenda o texto que já está no print.

DADOS REAIS (App Store do Brasil, consultados em 28/09/2026; não invente outros números)
- Nome na loja: Spotify: músicas e podcasts
- Nota: 4,9 de 5
- Avaliações: mais de 11 milhões (11.057.769)
- Descrição da loja: "biblioteca de músicas e podcasts de graça", playlists, "milhões de músicas"

NARRAÇÃO
Gere com `npx hyperframes tts --lang pt-br --voice pf_dora`, um arquivo por frase (audio/voz-1.wav a audio/voz-5.wav). Meça cada arquivo com ffprobe e ajuste a duração de cada cena para a fala caber, com 0,3 s de respiro.
1. "Músicas e podcasts em um só lugar."
2. "Playlists feitas para você, e a letra de cada música na tela."
3. "Os podcasts que você adora, no mesmo app."
4. "Nota quatro vírgula nove, com mais de onze milhões de avaliações."
5. "Baixe grátis agora."

CENAS (25 s no total)
1. 0 a 5 s: ícone entra no centro com bounce; título "Música e podcasts" palavra por palavra. Narração 1.
2. 5 a 10 s: print-4 sobe dentro da moldura do celular; print-3 entra atrás, deslocado (parallax). Chip "Playlists e letras". Narração 2.
3. 10 a 15 s: print-2 e print-1 lado a lado, com zoom lento (1,00 a 1,06). Narração 3.
4. 15 a 20 s: print-5 ao centro; selo com contagem de 0 até 4,9 e "+11 mi de avaliações" contando. Narração 4.
5. 20 a 25 s: ícone volta grande; botão desenhado "Baixar grátis agora" (sem logo da Apple). Narração 5.

ESTILO
Fundo escuro (#0b1220). Cor de destaque tirada do próprio ícone. Títulos grossos, palavra por palavra. Transições curtas (0,4 a 0,6 s) com ease power3.out.

ÁUDIO
Trilha com volume 0,25, fade-in de 0,5 s e fade-out de 1,5 s. Narração com volume 1,0, em data-track-index separado da trilha.

ENTREGA
1. Rode `npx hyperframes check` e corrija até não haver erros.
2. Renderize: `npx hyperframes render --format mp4 -o renders/spotify-demo.mp4`.
3. Tire 3 quadros (início, meio e fim) com `npx hyperframes snapshot` e me diga o que ficou diferente do combinado.
