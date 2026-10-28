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

## Rodada 3 · 28/out/2026

Cobre o que saiu depois da rodada 2 (27/out, 14h30) até 28/out, por volta das 17h20. Nenhuma regra mudou: não há emenda nesta rodada.

**O que entrou:**

- **58 fontes novas** (`dados/fontes_r3.csv`), 52 capturadas com sha256, e **31 citações conferidas** palavra por palavra (`dados/citacoes_r3.csv`, com teste). O levantamento, com as fontes de cada fato: [`dados/f4_estado_28out.md`](../dados/f4_estado_28out.md).
- **O relatório preliminar da OEA sobre o 2º turno** (27/out), lido no PDF da própria OEA por um script novo, `ferramentas/capturar_pdf.py`, com sha256.
- **A curva oficial da noite** (346 versões do resultado), do projeto do vídeo 16 (`d706893`), copiada com sha256 para `dados/derivados/video16/d5_curva_noite.csv`, para conferir a hora em que o resultado ficou definido.

**O que mudou:**

| Onde | Na rodada 2 | Na rodada 3 | Por quê |
|---|---|---|---|
| C4 · PF e observadores | sem dado | aponta L (parcial) | a OEA diz que não tem dúvidas quanto à integridade dos dados oficiais e que os resultados do TSE coincidem com o que os observadores coletaram; a PF não concluiu o inquérito sobre os ônibus |
| C3 · Justiça | aponta L (provisório) | sem mudança | nenhuma ação de cassação julgada; a carta do Flávio dizendo que a eleição foi roubada é fala, não ação |
| **Veredito de lente** | L na frente, sem prova para nenhum lado (4 de 5) | **o mesmo, com 5 de 5 critérios apontando L** | C3 provisório e C4 e C5 parciais impedem *L sustentada* (emenda 6) |
| S13 · asilo ou recusa de entregar o Flávio | L improvável | **L chance parecida** (fora da nota de Brier) | o Departamento de Estado anunciou vistos e entrada para o Flávio e a família, e ele entrou numa categoria de permissão temporária; a letra (asilo anunciado ou recusa de entrega) ainda não se cumpriu |
| S6 e S7 | improvável e provável | sem mudança | o Departamento de Estado falou do Brasil só para dar os vistos; o Trump disse que a eleição foi *"very strange"* e *"terrible"*, de novo sem a palavra que a letra pede |
| EUA · hipótese | H2 na frente, mais forte | H2 na frente, agora com um ato | o primeiro ato oficial depois da eleição foi o visto para o candidato que perdeu, não uma nota sobre o resultado |
| Círculo · H9 | o tom do círculo virou fala do presidente | sem ato novo vindo do círculo | o De Luca passou a pôr condição (investigar a prorrogação ou refazer o 2º turno); o Bannon pediu o rompimento; nada virou ato |

**A hora do pedido do passaporte** (pergunta do autor, a partir da frase *"7 minutos após o fim da apuração"*): a representação da PF foi assinada às **21h16** de 25/out, **7 minutos** depois de o TSE confirmar o resultado matematicamente (**21h09**); a curva oficial confirma que a definição aconteceu entre 21h08 e 21h09. A apuração só chegou a 100% às **23h26** (OEA), 2 horas e 10 minutos depois do pedido. O Moraes atendeu *"no domingo à noite"*, e o STF não informou a hora da decisão. A origem dos horários de 21h16 e 21h09 é uma coluna de *O Globo*, repetida por 5 veículos; a nota oficial da PF confirma só o dia. Detalhe na §1 do levantamento.

**O que segue aberto:** o julgamento das ações de cassação, a conclusão da PF sobre os ônibus e sobre a saída do Flávio, o consolidado do teste de integridade (C5), a nota do Departamento de Estado sobre o resultado, um pedido de asilo ou de extradição, e o relatório final da OEA.
