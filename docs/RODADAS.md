# As rodadas do projeto

O projeto é refeito por rodadas quando aparece dado novo. Cada rodada diz o que entrou, o que mudou e por quê. As regras ficam no [`PRE_REGISTRO.md`](PRE_REGISTRO.md); o que mudou nas regras depois de ver dado está nas emendas (§13), com a direção dita.

## Rodada 1 · 26/out/2026 (`0f72f8e` a `fc96373`)

Todas as fases do pré-registro (F0 a F7) com o que existia até a manhã de 26/out: 33 citações das primeiras horas, 25 eleições contestadas em duas passadas, os interesses medidos, a síntese das 12 suposições, o teste do passado e a revisão adversarial. Emendas 1 a 5. **Veredito de lente: aberto**, porque nenhum dos 5 critérios tinha dado.

## Rodada 2 · 27/out/2026

**O que entrou:**

- **Os números das urnas**, do projeto público do vídeo 16 (`investigacao-segundo-turno-2026`, `280d288`), copiados com sha256 para `dados/derivados/video16/`: 34.810 votos depois das 17h (0,79% da diferença), o RDV igual ao boletim em todas as seções comparadas, o log igual ao boletim em 99,7%, a abstenção caindo 1,86 ponto entre os turnos.
- **35 fontes novas** (`dados/fontes_r2.csv`), 30 capturadas com sha256, e 22 citações conferidas palavra por palavra (`dados/citacoes_r2.csv`, com teste). O levantamento, com as duas fontes de cada fato: [`dados/f4_estado_27out.md`](../dados/f4_estado_27out.md).
- **A emenda 6**, por decisão do autor: os arquivos das urnas baterem é o esperado nas duas lentes e pesam menos; *L sustentada* passa a exigir também C3 e C5 fechados.

**O que mudou:**

| Onde | Na rodada 1 | Na rodada 2 | Por quê |
|---|---|---|---|
| C1 · prorrogação | sem dado | aponta L | 34.810 votos depois das 17h, 0,79% da diferença |
| C2 · arquivos das urnas | sem dado | aponta L (menor peso) | RDV e log batem com o boletim |
| C3 · Justiça | sem dado | aponta L (provisório) | o Flávio desistiu da anulação e o PL reconheceu; as ações de cassação não foram julgadas |
| C4 · PF e observadores | sem dado | sem dado | sem conclusão da PF; a OEA não publicou relatório do 2º turno |
| C5 · teste de integridade | sem dado | aponta L (parcial) | TSE e São Paulo sem divergência; falta o consolidado |
| **Veredito de lente** | aberto | **L na frente, sem prova para nenhum lado** | pela emenda 6; sem ela, a regra original daria *L sustentada* |
| S1 · anulação | L muito improvável | L quase nenhuma chance | desistência do próprio Flávio |
| S6 · Departamento de Estado trata como válido | L chance parecida | L improvável | a nota ficou pronta e foi adiada, segundo a Folha |
| S7 · EUA falam em fraude | L improvável | L provável | o Trump disse que a eleição pareceu fraudada; pela letra do critério ainda não resolve |
| S9 · mensagem do Xi | L provável | aconteceu | mensagem pessoal em 27/out |
| S13 · asilo ou recusa de entregar o Flávio | não existia | L improvável (fora da nota de Brier) | o caso do passaporte e o relato de aliados sobre a saída para os EUA |
| EUA · hipótese | H2 na frente | H2 na frente, mais forte | a fala do Trump repete o padrão de Honduras 2025 com o sinal trocado |
| Círculo · H9 | o círculo antecipa o tom | o tom do círculo virou fala do presidente, sem ato oficial | De Luca em 25/out, Trump em 26/out |

**O que segue aberto:** C4 (PF e OEA), o consolidado de C5, o julgamento das ações de cassação, a nota do Departamento de Estado e o paradeiro do Flávio. As suposições resolvem nas datas da §8 do pré-registro (02/nov, 25/nov, 05/jan/2027 e fim de 2027).
