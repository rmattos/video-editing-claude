/product-launch-video

Crie um vídeo promocional vertical (1080x1920) de 25 segundos do app Duolingo, para Reels, Shorts e TikTok. É uma demonstração NÃO oficial feita com o material público da loja de apps.

REGRAS
- Não rode `hyperframes capture` e não baixe nada da internet: use somente os arquivos listados abaixo, que já estão na pasta do projeto.
- Todo texto na tela e toda a narração em português do Brasil. Sem emoji.
- Sem rosto, pessoa ou cena filmada: só o ícone, os prints e elementos gráficos feitos em HTML, CSS e GSAP.
- Fonte sem serifa que já exista no computador (Arial ou Segoe UI); não carregue fonte da internet.
- Composição determinística: sem Date.now(), sem Math.random(), sem fetch de rede.
- Selo pequeno no canto superior durante o vídeo inteiro: "Demonstração não oficial · sem vínculo com Duolingo".

ARQUIVOS (já estão na pasta do projeto)
- assets/duolingo/icone.jpg: ícone do app, 1024x1024
- assets/duolingo/print-1.jpg: escolha de idioma (mais de 40 idiomas)
- assets/duolingo/print-2.jpg: exercício de traduzir
- assets/duolingo/print-3.jpg: lições curtinhas, com o mascote
- assets/duolingo/print-4.jpg: falar e ouvir no novo idioma
- assets/duolingo/print-5.jpg: vocabulário novo
- audio/trilha-app.mp3: trilha de fundo, 112 bpm, 28 s
Cada print é um retrato com texto e fundo colorido próprios da loja. Mostre inteiro (object-fit: contain) dentro de uma moldura de celular desenhada em CSS; não corte, não distorça e não repita na legenda o texto que já está no print.

DADOS REAIS (App Store do Brasil, consultados em 28/09/2026; não invente outros números)
- Nome na loja: Duolingo – Aprenda idiomas
- Nota: 4,9 de 5
- Avaliações: mais de 1,1 milhão (1.149.571)
- Descrição da loja: "lições rápidas e curtinhas", "mais de 40 línguas", app "grátis" para baixar

NARRAÇÃO
Gere com `npx hyperframes tts --lang pt-br --voice pf_dora`, um arquivo por frase (audio/voz-1.wav a audio/voz-5.wav). Meça cada arquivo com ffprobe e ajuste a duração de cada cena para a fala caber, com 0,3 s de respiro.
1. "Aprender um idioma em lições rápidas e curtinhas."
2. "Mais de quarenta línguas para escolher."
3. "Escute, fale e treine o vocabulário."
4. "Nota quatro vírgula nove, com mais de um milhão de avaliações."
5. "Baixe grátis agora."

CENAS (25 s no total)
1. 0 a 5 s: ícone entra no centro com bounce; título "Aprenda idiomas" palavra por palavra. Narração 1.
2. 5 a 10 s: print-1 sobe dentro da moldura do celular; print-2 entra atrás, deslocado (parallax). Chip "+40 idiomas". Narração 2.
3. 10 a 15 s: print-4 e print-5 lado a lado, com zoom lento (1,00 a 1,06). Narração 3.
4. 15 a 20 s: print-3 ao centro; selo com contagem de 0 até 4,9 e "+1,1 mi de avaliações" contando. Narração 4.
5. 20 a 25 s: ícone volta grande; botão desenhado "Baixar grátis agora" (sem logo da Apple). Narração 5.

ESTILO
Fundo escuro (#0b1220). Cor de destaque tirada do próprio ícone. Títulos grossos, palavra por palavra. Transições curtas (0,4 a 0,6 s) com ease power3.out.

ÁUDIO
Trilha com volume 0,25, fade-in de 0,5 s e fade-out de 1,5 s. Narração com volume 1,0, em data-track-index separado da trilha.

ENTREGA
1. Rode `npx hyperframes check` e corrija até não haver erros.
2. Renderize: `npx hyperframes render --format mp4 -o renders/duolingo-demo.mp4`.
3. Tire 3 quadros (início, meio e fim) com `npx hyperframes snapshot` e me diga o que ficou diferente do combinado.
