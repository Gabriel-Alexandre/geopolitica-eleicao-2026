# Revisão adversarial: o defensor da lente F

**Papel:** defender, da forma mais forte e honesta possível, a lente F do pré-registro (o resultado do 2º turno de 25/out/2026, Lula 51,79% × Flávio 48,21%, não reflete a vontade do eleitor), e apontar onde o projeto foi injusto com ela. Escrito em 26/out/2026 pelo Claude, como leitor adversarial pedido pela §10 do pré-registro.

**O que foi lido:** `docs/PRE_REGISTRO.md` (com as emendas 1 a 3), `RELATORIO.md`, `docs/LEITURA_DA_IA.md`, `docs/F1_REACOES.md`, `docs/F4_CONTESTACAO.md`, `dados/f4_estado_26out.md`, `dados/sintese_suposicoes.csv`, `dados/hipoteses_veredito.csv`, `dados/criterios_c1_c5.csv`, `resultados/f2_taxas_base.csv`, `resultados/f2_concordancia.csv`, `resultados/f2_casos_consenso.json` e as quatro passadas em `dados/casos/`.

**O que foi conferido fora do repositório:** uma página só, a da eleição presidencial da Áustria de 2016 na Wikipedia (anulação do 2º turno em 01/jul/2016 por irregularidade de procedimento, *"no indication of fraud was found"*, cerca de 77.900 votos por correspondência contados antes da hora contra uma margem de 30.863). É uma fonte só, e enciclopédica: vale como pista para a ficha, não como ficha. Nada mais foi conferido na internet nesta revisão; os fatos dos casos históricos citados abaixo vêm das próprias fichas do projeto.

**O que esta revisão não afirma:** que houve fraude. Ela mede se o projeto aplicou à lente F a mesma régua que aplicou à lente L.

---

## 1. Onde o projeto conta a favor de L o que a própria régua não sustenta

### 1.1 O C3 aponta L com 14 horas de prazo, contra o próprio levantamento

O `dados/f4_estado_26out.md` §1 termina com: *"C3 hoje: sem dado (ação não proposta até 10h05). [...] o critério fica aberto."* O `dados/criterios_c1_c5.csv`, o `RELATORIO.md` §1 e §3 e o `docs/F4_CONTESTACAO.md` codificam o mesmo C3 como `L_provisorio`, e o veredito publicado diz *"2 de 5 critérios apontam L (C3, C5)"*. São dois estados para o mesmo fato.

O pré-registro diz que C3 aponta L se a ação for *"julgada improcedente ou não proposta"*. Ler "não proposta" como "não proposta até a manhã seguinte", quando o próprio Flávio anunciou na noite anterior que vai propor, transforma um prazo de horas em resultado. A leitura justa de "não proposta" é "não proposta no prazo legal para contestar o resultado". E a única informação de mérito citada na linha do C3 é a avaliação de ministros ouvidos em reserva pelo g1, que pela §11 do pré-registro entra como *"segundo o g1"*, nunca como base de critério.

### 1.2 O C5 aponta L sem nenhuma linha conferida em duas fontes

No `dados/f4_estado_26out.md` §3, as cinco linhas do teste de integridade têm *"Conferido em duas fontes: não"*. O número 389 do TSE e o *"sem divergências"* de SP, MT e SC vêm de **resumo de busca** (as páginas devolveram HTTP 403), e a §9 do pré-registro diz que resumo automático não é fonte. A única linha lida em texto é a do Distrito Federal, com uma fonte só, e ela relata **uma divergência**, que a própria auditoria classificou como erro humano de digitação. Pela régua do projeto, o C5 hoje é *sem dado*, e o fato lido em texto é uma divergência explicada pela parte auditada.

Isso não quer dizer que o teste falhou. Quer dizer que o projeto contou como *"aponta L (parcial)"* um critério que, pela regra de fonte que ele aplica a todo o resto, não tem dado.

**Efeito conjunto de 1.1 e 1.2:** o veredito continua *aberta*, mas a frase pública muda de *"2 de 5 critérios apontam L, nenhum aponta F"* para *"0 de 5 apontam L, 0 de 5 apontam F, 5 sem dado"*. Para quem lê só a primeira tabela do relatório, é a diferença entre "a evidência pende para L" e "ainda não há evidência".

### 1.3 O C1 mede o lado errado da prorrogação

O argumento do Flávio (citado no próprio `f4_estado` §1 e §6) é de **isonomia**: seções que fecharam às 17h antes do aviso do TSE (17h49, Poder360) e não reabriram, urnas desligadas no Rio, eleitores com *"declaração de comparecimento sem voto"* (DCM). O dano alegado são os **votos que não puderam ser dados** onde a prorrogação não chegou.

O C1, como está escrito, mede os **votos acrescentados** depois das 17h onde a prorrogação chegou. O número de imprensa que o projeto usa como contraponto (35.521 votos depois das 17h, g1) mede a mesma coisa. Nenhum dos cinco critérios mede exclusão: abstenção das seções fechadas contra a abstenção das mesmas seções no 1º turno, ou contra seções parecidas que ficaram abertas. O mesmo buraco vale para a queixa do outro lado (falta de ônibus): ela também é exclusão, e também não tem critério. Ou seja, a lente F perde o seu argumento mais concreto por desenho, e a lente "fraude a favor do Flávio" perde o dela pelo mesmo motivo.

**Variante calculável (C1b, teto da exclusão no pior caso):** votos que deixaram de ser dados nas seções fechadas = (votos depois das 17h ÷ seções que ficaram abertas depois das 17h) × seções que fecharam antes do aviso, todos de um lado só, como o C1 faz. Com os números do g1 (35.521 votos, 497.897 seções), esse teto **alcança a diferença de 4.430.191 se menos de cerca de 3.960 seções (0,8%) ficaram abertas depois das 17h**. O projeto não sabe esse número: o `f4_estado` §4 registra *"Número de seções que ficaram abertas depois das 17h: não encontrado"*. Os logs que a emenda 3 espera do `investigacao-segundo-turno-2026` dão o número exato.

Ressalva que o defensor tem de fazer: a extrapolação é generosa com F, porque as seções que ficaram abertas tinham fila, e as que fecharam provavelmente não; e o C1 do pré-registro ainda exige que o perfil dos votos diverja. O C1b é um teto, como o C1, e não uma estimativa.

### 1.4 O número do g1 "não é usado", mas é usado contra o lado do Flávio

O `criterios_c1_c5.csv` e a emenda 3 dizem que os 35.521 votos não substituem o C1, porque o número é cem vezes menor que a fila do 1º turno medida nos logs (3,72 milhões depois das 17h). Mesmo assim, o `f4_estado` §6, na linha da alegação de quebra de isonomia, escreve *"Contra o efeito: 35.521 votos depois das 17h = 0,8% da diferença (g1)"*, e o `RELATORIO.md` §3 repete que o número *"daria 0,8% da diferença no pior caso"*. Um número que o projeto declara não confiável para o critério aparece como a única resposta quantitativa à principal alegação de F, e mede outra coisa (ver 1.3).

### 1.5 A discrepância de cem vezes tem duas leituras, e o projeto considera uma

O projeto lê a distância entre 3,72 milhões (1º turno, logs) e 35.521 (2º turno, g1) como sinal de que o g1 contou outra coisa. É a leitura mais provável. A outra leitura, que a lente F tem o direito de pedir que seja testada, é que a queda é real: se no 2º turno votaram depois das 17h cerca de 3,68 milhões de pessoas a menos do que no 1º, isso é **83% da diferença** (3.684.479 ÷ 4.430.191). Mesmo nesse pior caso, e mesmo supondo que todos seriam votos de um lado só, o número fica **abaixo** da diferença; mas fica longe de *"imaterial"*. A pergunta é barata de responder com os logs, e o relatório deveria dizer que ela existe.

### 1.6 A resposta do TSE sobre a sala-cofre conta como duas fontes

Na alegação dos fiscais do PL retirados da sala-cofre, o `f4_estado` §6 marca *"Conferido em duas fontes: sim"* com Metrópoles e CNN Brasil, e registra a resposta do TSE (*"é falso"*). As duas matérias reproduzem a mesma nota do TSE, que é a parte acusada. No caso do g1 o projeto teve o cuidado de escrever *"uma origem, repetida"*; aqui não. O correto é: a alegação tem uma origem (o Flávio) e a negativa tem uma origem (o TSE), e nenhum terceiro (fiscal do PL identificado, OEA) foi lido.

---

## 2. A classe de referência

### 2.1 "Nenhuma eleição sem fraude demonstrada foi anulada" é verdade por codificação

O `RELATORIO.md` e a `LEITURA_DA_IA.md` (S1) afirmam: *"Nenhuma eleição sem fraude demonstrada foi anulada no histórico"* (0 de 10). Isso depende de três escolhas:

| Caso | O que a ficha do projeto diz | Como entrou na conta |
|---|---|---|
| Quênia 2017 | a Suprema Corte anulou *"por irregularidades e ilegalidades na transmissão [...] sem atribuir fraude a Kenyatta"*; observadores *"validaram"* (passada A) | `fraude_demonstrada = disputado`, grupo F |
| Malaui 2019 | anulada por *"irregularidades generalizadas (atas alteradas, corretivo)"*; estudo de 2025 conclui *"compatíveis com erro humano, não fraude intencional"* | divergente (A: `disputado`, B: `sim`), fora dos dois grupos |
| Áustria 2016 | não tem ficha | fora da lista, embora o perdedor tenha contestado e o tribunal tenha anulado o 2º turno por procedimento, sem fraude (conferido só na Wikipedia) |

Esses três são exatamente a categoria que o argumento do Flávio invoca: **anulação por irregularidade de procedimento, sem fraude provada**. O código binário (fraude demonstrada ou disputada × não) empurra essa categoria para o lado F ou para fora, e por isso ela vale zero na lente L. A própria definição da lente L (*"os problemas de procedimento [...] são reais e não mudaram quem ganhou"*) não exclui que um tribunal anule por procedimento; foi o que aconteceu na Áustria.

**Variantes calculáveis da taxa `anulada_ou_refeita | lente L`:**

| Variante | Conta | Faixa da S1 em L |
|---|---|---|
| atual | 0 de 10 (0%) | quase nenhuma chance |
| Malaui 2019 recodificado `nao` | 1 de 11 (9%) | muito improvável |
| + Quênia 2017 recodificado `nao` | 2 de 12 (17%) | muito improvável |
| + Áustria 2016 com ficha, se passar na regra de entrada | 3 de 13 (23%) | improvável |

Ressalva honesta: a Áustria pode não passar na regra de entrada da §5 (*"eleição nacional que define o governo"*: o presidente austríaco não chefia o governo), e a Justiça brasileira já rejeitou em 2022 um pedido de anulação parcial com multa por litigância de má-fé (registrado no `f4_estado` §1, só em resumo de busca). A margem de 2026 também é dezenas de vezes maior que a austríaca. Mas isso é ajuste do caso, que o método de Tetlock manda fazer **depois** de uma taxa-base honesta, e não motivo para a taxa-base ser zero.

### 2.2 A regra de divergência da emenda 2 foi aplicada no campo errado

A emenda 2 tira da taxa o campo em que as passadas discordam. No Malaui, as passadas discordam entre `disputado` e `sim`, mas **as duas o põem no grupo F** ("fraude demonstrada ou disputada"), que é a única coisa que o agrupamento usa. O caso saiu dos dois grupos por uma divergência que não muda o grupo. Com a regra aplicada ao grupo, o Malaui entra no F: anulada 4 de 7, posse 5 de 7. É uma correção pequena, mas é a regra escrita aplicada à variável que de fato entra na conta.

### 2.3 A exclusão por falta de fonte cai quase toda do lado F

Dos 6 casos excluídos por não fecharem com duas fontes, **5 são do lado F** nas duas passadas (Costa do Marfim 2010, Geórgia 2003, Honduras 2017, Sérvia 2000, Ucrânia 2004) e 1 do lado L (Venezuela 2013). A causa registrada é a cota de buscas e páginas que não abriram (a Ucrânia 2004 fecha na passada B e não na A, por *"a cota de buscas da passada acabou"*), não dúvida sobre os fatos. Os casos mais antigos, os da era em que fraude demonstrada derrubou o vencedor anunciado, são os que mais sofrem com fonte escassa na internet. O grupo F ficou com 6 casos, contra 10 do L.

Efeito medido nesta revisão, refazendo a conta com os 6 casos de volta (campo a campo, só onde as duas passadas concordam): **as taxas mudam pouco** (anulada no grupo F de 50% para 45%; posse de 67% para 64%; violência de 83% para 73%). O defensor de F tem de registrar que a exclusão não distorce os números. Ela distorce uma frase: a `LEITURA_DA_IA.md` (S4) diz que *"os não reconhecimentos do histórico têm todos o vencedor como adversário dos EUA"*. Na Ucrânia 2004, a ficha do projeto codifica o vencedor anunciado como **neutro** para os EUA, e Colin Powell disse que o resultado *"não pode ser aceito como legítimo"*. A frase só é verdadeira porque o caso saiu.

---

## 3. Calibração das faixas F1 e F2

### 3.1 A coluna F1 não foi revista contra as taxas do próprio grupo F

Na `sintese_suposicoes.csv`, as colunas L e F2 mudaram em S7, S8, S9 e S11; a coluna F1 não mudou em nenhuma linha. Em várias, ela contradiz a taxa do grupo F que o projeto mesmo publica:

| Suposição | F1 publicada | O que o grupo F do projeto mostra | Faixa que a taxa sugere |
|---|---|---|---|
| S9 · Xi manda mensagem pessoal | improvável (20 a 45%) | China parabenizou em 3 de 3 casos do grupo F; a H5 diz que a China segue a autoridade eleitoral *"nas duas lentes"* | provável ou muito provável (ajustado pelo nível pessoal, como foi feito em L) |
| S10 · Putin parabeniza | improvável | Rússia parabenizou em 2 de 2 (3 de 3 com a Ucrânia 2004) | muito provável |
| S8 · nova medida dos EUA | quase certo (95 a 99%) | sanção ligada à eleição em 3 de 6 (50%); com vencedor neutro, 0 de 1 | chance parecida a provável |
| S4 · os EUA continuam tratando o governo Lula como o governo | improvável | não reconhecimento em 2 de 5 (40%), então continuar em 60%; e o Lula é o presidente em exercício até 05/jan/2027 em qualquer lente | provável |

Por que isso é injusto com F: pela §8, a nota de Brier é calculada com a coluna da lente que o veredito apontar. Se um dia o veredito for F1, a coluna F1 será julgada com faixas que o próprio histórico do projeto não sustenta, e a lente vai parecer pior do que é. A coluna L foi recalibrada pelo dado; a F1 ficou com a primeira leitura.

### 3.2 O nome do veredito "L sustentada" diz mais do que os critérios medem

A §2 já reconhece que F2 é o mundo em que boletins, logs, totalização e teste de integridade fecham. Logo, C2 e C5 apontando L é o esperado **também** em F2: esses critérios só conseguem derrubar F1. A regra da §3 chama de *"L sustentada"* o caso em que C1 e C2 apontam L; o nome correto do que os critérios mostram nesse caso é *"F1 rejeitada; L e F2 indistinguíveis por dado"*. O pré-registro diz isso sobre F2 em outro lugar; o rótulo do veredito e a frase *"2 de 5 apontam L"* não dizem. Não muda conta nenhuma, muda o que o leitor entende que foi provado.

### 3.3 O que está bem calibrado (para registro)

- S1 em F1 (*provável*): com o grupo F restrito a países sem tribunal capturado (Bolívia 2019, Quênia 2007, Quênia 2017, Romênia 2024, Malaui 2019), a anulação fica em 4 de 5; a faixa poderia subir para *muito provável*, mas a definição de F1 aceita prova validada só por observadores, sem a Justiça, e então *provável* é defensável.
- F2 igual a L: coerente com a definição (governo estrangeiro reage ao que dá para mostrar).
- S7: o projeto não contou a fala do Trump pela EFE (*"manual de Joe Biden"*) como resolução, por não usar as palavras do critério. É a leitura estrita e conservadora, e a lente F não tem do que reclamar aqui.
- A apuração da Reuters sobre o Departamento de Estado entrou como *"segundo a Reuters"*, com a negativa ao lado: tratamento igual para os dois lados.

---

## 4. Tabela das objeções

| Objeção | Onde está no projeto | O que muda se a objeção estiver certa | Gravidade |
|---|---|---|---|
| C1 mede os votos que a prorrogação acrescentou, não os que deixou de acrescentar nas seções fechadas antes do aviso; nenhum critério mede exclusão (isso vale também para a falta de ônibus) | `PRE_REGISTRO.md` §3 (C1); `f4_estado_26out.md` §4 e §6 | entra um C1b; com os números do g1, o teto da exclusão alcança 4.430.191 se menos de ~3.960 seções (0,8%) ficaram abertas depois das 17h, número que o projeto não tem | alta |
| C3 contado como L com 14 h de prazo e com o próprio levantamento dizendo *"sem dado"* | `criterios_c1_c5.csv`; `RELATORIO.md` §1 e §3; contra `f4_estado_26out.md` §1 | C3 vira *sem dado* até o fim do prazo legal de contestação | alta |
| C5 contado como L sem nenhuma linha conferida em duas fontes; a única leitura em texto (DF) mostra uma divergência | `criterios_c1_c5.csv`; `f4_estado_26out.md` §3 | C5 vira *sem dado*; o veredito publicado passa de "2 de 5 apontam L" para "0 de 5" | alta |
| "Nenhuma eleição sem fraude demonstrada foi anulada" depende de codificar anulação por procedimento como F (Quênia 2017), tirar o Malaui por divergência e não ter a Áustria 2016 | `f2_casos_consenso.json`; `f2_taxas_base.csv`; `LEITURA_DA_IA.md` S1 | `anulada_ou_refeita | L` vai de 0% para 9%, 17% ou 23%; S1 em L sai de *quase nenhuma chance* para *muito improvável* ou *improvável* | alta |
| O número do g1 é declarado inutilizável para o C1 e usado como contra-argumento à alegação de isonomia | `f4_estado_26out.md` §6; `RELATORIO.md` §3 | sai da linha "contra o efeito", ou entra com a ressalva de que mede outra coisa | média |
| A discrepância 3,72 mi × 35.521 só é lida como erro de medida do g1; a queda real (3,68 mi, 83% da diferença) não é testada | emenda 3; `criterios_c1_c5.csv` | o relatório registra a pergunta e o teste nos logs; no pior caso ainda fica abaixo da diferença | média |
| Coluna F1 não recalibrada contra o grupo F (S4, S8, S9, S10) | `sintese_suposicoes.csv` | S9 e S10 em F1 sobem; S8 desce; S4 sobe; a nota de Brier de F1, se um dia contar, deixa de ser punida por faixa sem lastro | média |
| A emenda 2 tirou o Malaui por divergência num campo que não muda o grupo | `f2_casos_consenso.json` (malaui-2019 `divergente`) | Malaui entra no grupo F: anulada 4 de 7, posse 5 de 7 | baixa |
| 5 dos 6 casos excluídos por fonte são do lado F, por cota de busca e não por dúvida de fato | emenda 2; `RELATORIO.md` (casos fora) | taxas mudam pouco; cai a frase da S4 de que todo não reconhecimento teve vencedor adversário (Ucrânia 2004, vencedor neutro) | média (a frase) · baixa (as taxas) |
| "L sustentada" é o nome de um veredito que só consegue rejeitar F1; L e F2 ficam indistinguíveis | `PRE_REGISTRO.md` §3; `RELATORIO.md` §1 | rótulo vira "F1 rejeitada; L e F2 não se distinguem por dado" | média |
| A negativa do TSE sobre a sala-cofre conta como duas fontes, mas é uma origem, e é a parte acusada | `f4_estado_26out.md` §6 | marca "uma origem" e "sem terceiro lido", como foi feito no g1 | baixa |

---

## 5. A objeção mais forte

**O projeto só mede os votos que a prorrogação acrescentou e nunca os que ela deixou de permitir nas seções fechadas antes do aviso das 17h49, que é a alegação de F; a variante é um C1b, o teto da exclusão no pior caso, igual a (votos depois das 17h ÷ seções abertas depois das 17h) × seções fechadas antes do aviso, todos de um lado só, que com os números do g1 alcança a diferença de 4.430.191 se menos de cerca de 3.960 seções (0,8% de 497.897) ficaram abertas depois das 17h, e que os logs do `investigacao-segundo-turno-2026` resolvem com o número exato.**

A segunda mais forte, e a única calculável hoje sem dado novo: recodificar Malaui 2019 e Quênia 2017 como `fraude_demonstrada = nao` e refazer `anulada_ou_refeita | lente L`, que vai de 0 de 10 para 2 de 12 (17%) e tira a S1 em L de *quase nenhuma chance*.
