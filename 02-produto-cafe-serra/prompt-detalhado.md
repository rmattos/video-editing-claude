/music-to-video

Crie um vídeo quadrado (1080x1080) de 15 segundos para o Instagram divulgando o Café Serra, um café especial. A marca é fictícia, criada só para este exemplo: mantenha um selo pequeno "exemplo fictício" no canto durante o vídeo todo.

REGRAS
- Não baixe nada da internet: use somente os arquivos listados abaixo, que já estão na pasta do projeto.
- Todo texto na tela em português do Brasil. Sem emoji. Sem pessoas.
- Fonte sem serifa que já exista no computador (Arial ou Segoe UI).
- Composição determinística: sem Date.now(), sem Math.random(), sem fetch de rede.

ARQUIVOS (já estão na pasta do projeto)
- fotos/foto-1.png: xícara sobre a mesa, com vapor (foto principal)
- fotos/foto-2.png: close da xícara
- fotos/foto-3.png: vista de cima, com coração na espuma
- fotos/foto-4.png: pacote "SERRA café especial" com a xícara e grãos
- fotos/foto-5.png: xícara sobre livros, ao lado da janela
- fotos/foto-6.png: xícara em fundo limpo
Todas 1080x1080. Mostre cada uma em tela cheia (object-fit: cover).
- audio/trilha-cafe.mp3: trilha de fundo, 92 bpm, 15,6 s. Marque o elemento de áudio com id="music" e data-timeline-role="music".

SINCRONIA COM A MÚSICA
- Rode `npx hyperframes beats`. Ele grava beats/audio/trilha-cafe.mp3.json com o tempo e a força de cada batida. O detector marca o dobro do andamento real (cerca de 184 em vez de 92): isso é esperado, não corrija.
- Troque de foto a cada 4 marcações (cerca de 1,3 s), nesta ordem: 1, 2, 3, 4, 5, 6, 2, 4, 1, 5, 3, 6.
- Em cada troca, um pulso rápido: escala 1,00 para 1,04 e volta, em 0,25 s.
- Nas 3 batidas de maior "strength", um flash branco de 0,1 s.
- Durante o tempo em tela, cada foto faz um zoom lento de 1,00 a 1,08, alternando o sentido a cada foto.

TEXTOS
- 0 a 2,6 s: "SERRA" grande e, abaixo, "café especial".
- 3,9 a 6,5 s: "Torrado em pequenos lotes".
- 7,8 a 10,4 s: "Moído na hora, servido quente".
- 11 a 15 s: "Peça o seu" e, abaixo, "serra.exemplo".
Cor #f6ead9 sobre um degradê escuro na parte de baixo da tela, para ler bem em cima das fotos claras.

ÁUDIO
Trilha com volume 0,8, fade-in de 0,3 s e fade-out de 1,5 s (termina junto com o vídeo, aos 15 s).

ENTREGA
1. Rode `npx hyperframes check` e corrija até não haver erros.
2. Renderize: `npx hyperframes render --format mp4 -o renders/cafe-serra.mp4`.
3. Tire 3 quadros (início, meio e fim) com `npx hyperframes snapshot` e me diga o que ficou diferente do combinado.
