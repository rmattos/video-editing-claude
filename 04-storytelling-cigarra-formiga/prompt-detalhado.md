/faceless-explainer

Crie um vídeo narrado de cerca de 50 segundos, horizontal (1920x1080), contando a fábula "A cigarra e a formiga" (de Esopo, domínio público), em português do Brasil, sem rosto nem pessoa filmada.

REGRAS
- Não baixe nada da internet: use somente os arquivos listados abaixo, que já estão na pasta do projeto.
- Use o texto de roteiro.txt exatamente como está, sem reescrever.
- Sem emoji. Fonte sem serifa que já exista no computador (Arial ou Segoe UI).
- Composição determinística: sem Date.now(), sem Math.random(), sem fetch de rede.

ARQUIVOS (já estão na pasta do projeto)
- roteiro.txt: 5 parágrafos separados por linha em branco
- cenas/cena-1.png: verão, a cigarra cantando no galho
- cenas/cena-2.png: a formiga carregando um grão
- cenas/cena-3.png: inverno, a cigarra com frio na neve
- cenas/cena-4.png: a porta do formigueiro acesa e a cigarra do lado de fora
Todas 1920x1080.
- audio/trilha-historia.mp3: trilha suave de 80 s, 72 bpm; use os primeiros 50 s.

NARRAÇÃO
Gere com `npx hyperframes tts --lang pt-br --voice pf_dora`, um arquivo por parágrafo (audio/par-1.wav a audio/par-5.wav). Meça cada arquivo com ffprobe: a duração de cada cena é a duração da fala mais 0,6 s.

MAPA DE CENAS
- Parágrafo 1: cena-1
- Parágrafo 2: cena-2
- Parágrafo 3: cena-3
- Parágrafo 4: cena-4
- Parágrafo 5 (a moral): cena-4 com escurecimento de 40% e o texto da moral em destaque no alto da tela, centralizado na horizontal.

MOVIMENTO
- Cada imagem faz um zoom lento de 1,00 a 1,10 com deslocamento de no máximo 4%, alternando o sentido a cada cena.
- Troca entre cenas com cross-fade de 0,6 s.

TEXTOS
- 0 a 3 s: título "A cigarra e a formiga" e, abaixo, "Fábula de Esopo, recontada". Esse título aparece por cima da cena-1 e a narração do parágrafo 1 começa depois dele.
- Legendas frase por frase na parte inferior, fonte de 54 px, fundo preto com 55% de opacidade, sincronizadas com a fala (divida a duração do parágrafo proporcionalmente ao número de caracteres de cada frase).

ÁUDIO
Trilha com volume 0,18 durante a fala, fade-in de 1,5 s e fade-out de 3 s no final (aos 50 s). Narração com volume 1,0, em data-track-index separado.

ENTREGA
1. Rode `npx hyperframes check` e corrija até não haver erros.
2. Renderize: `npx hyperframes render --format mp4 -o renders/cigarra-formiga.mp4`.
3. Tire 3 quadros (início, meio e fim) com `npx hyperframes snapshot` e me diga o que ficou diferente do combinado.
