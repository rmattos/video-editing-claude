/product-launch-video

Crie um vídeo promocional vertical (1080x1920) de 25 segundos do app iFood, para Reels, Shorts e TikTok. É uma demonstração NÃO oficial feita com o material público da loja de apps.

REGRAS
- Não rode `hyperframes capture` e não baixe nada da internet: use somente os arquivos listados abaixo, que já estão na pasta do projeto.
- Todo texto na tela e toda a narração em português do Brasil. Sem emoji.
- Sem rosto, pessoa ou cena filmada: só o ícone, os prints e elementos gráficos feitos em HTML, CSS e GSAP.
- Fonte sem serifa que já exista no computador (Arial ou Segoe UI); não carregue fonte da internet.
- Composição determinística: sem Date.now(), sem Math.random(), sem fetch de rede.
- Selo pequeno no canto superior durante o vídeo inteiro: "Demonstração não oficial · sem vínculo com iFood".

ARQUIVOS (já estão na pasta do projeto)
- assets/ifood/icone.jpg: ícone do app, 1024x1024
- assets/ifood/print-1.jpg: delivery de mercado, restaurante, bebidas, farmácia e pet shop
- assets/ifood/print-2.jpg: opções de restaurantes
- assets/ifood/print-3.jpg: filtros para facilitar a busca
- assets/ifood/print-4.jpg: fazer mercado sem sair de casa
- assets/ifood/print-5.jpg: comprar bebidas em poucos cliques
- audio/trilha-app.mp3: trilha de fundo, 112 bpm, 28 s
Cada print é um retrato com texto e fundo colorido próprios da loja. Mostre inteiro (object-fit: contain) dentro de uma moldura de celular desenhada em CSS; não corte, não distorça e não repita na legenda o texto que já está no print.

DADOS REAIS (App Store do Brasil, consultados em 28/09/2026; não invente outros números)
- Nome na loja: iFood: pedir delivery em casa
- Nota: 4,9 de 5
- Avaliações: cerca de 8,9 milhões (8.868.952)
- Descrição da loja: "mercados, restaurantes, farmácias e pet shop", "de forma fácil e rápida"

NARRAÇÃO
Gere com `npx hyperframes tts --lang pt-br --voice pf_dora`, um arquivo por frase (audio/voz-1.wav a audio/voz-5.wav). Meça cada arquivo com ffprobe e ajuste a duração de cada cena para a fala caber, com 0,3 s de respiro.
1. "Mercado, restaurante, farmácia e pet shop em um só app."
2. "Explore restaurantes e use os filtros para achar rápido."
3. "Faça mercado e peça bebidas em poucos cliques."
4. "Nota quatro vírgula nove, com quase nove milhões de avaliações."
5. "Baixe grátis na App Store."

CENAS (25 s no total)
1. 0 a 5 s: ícone entra no centro com bounce; título "Tudo em um só app" palavra por palavra. Narração 1.
2. 5 a 10 s: print-2 sobe dentro da moldura do celular; print-3 entra atrás, deslocado (parallax). Chip "Filtros". Narração 2.
3. 10 a 15 s: print-4 e print-5 lado a lado, com zoom lento (1,00 a 1,06). Narração 3.
4. 15 a 20 s: print-1 ao centro; selo com contagem de 0 até 4,9 e "+8,9 mi de avaliações" contando. Narração 4.
5. 20 a 25 s: ícone volta grande; botão desenhado "Baixar grátis na App Store" (sem logo da Apple). Narração 5.

ESTILO
Fundo escuro (#0b1220). Cor de destaque tirada do próprio ícone. Títulos grossos, palavra por palavra. Transições curtas (0,4 a 0,6 s) com ease power3.out.

ÁUDIO
Trilha com volume 0,25, fade-in de 0,5 s e fade-out de 1,5 s. Narração com volume 1,0, em data-track-index separado da trilha.

ENTREGA
1. Rode `npx hyperframes check` e corrija até não haver erros.
2. Renderize: `npx hyperframes render --format mp4 -o renders/ifood-demo.mp4`.
3. Tire 3 quadros (início, meio e fim) com `npx hyperframes snapshot` e me diga o que ficou diferente do combinado.
