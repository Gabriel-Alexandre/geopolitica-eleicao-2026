# Rodada 2 · o estado dos critérios e das reações em 27/out/2026

**Busca feita em 27/out/2026, até cerca de 14h30 (horário de Brasília).** Cada citação abaixo está em `dados/citacoes_r2.csv` e foi conferida palavra por palavra no texto capturado com sha256 (`dados/capturas/r2_*.txt`, registro em `dados/MANIFESTO.json`; o teste `test_rodada_2_toda_citacao_esta_no_texto_capturado_com_hash` refaz a conferência). Das 35 fontes da lista `dados/fontes_r2.csv`, 30 foram capturadas; as 5 que recusaram leitura (HTTP 403) aparecem marcadas.

Os números das urnas vêm do projeto público do vídeo 16, `investigacao-segundo-turno-2026` (commit `280d288`), copiados com sha256 para `dados/derivados/video16/`:

| Arquivo copiado | sha256 |
|---|---|
| `rodada2.json` | `a8aab560b8f56b6a5b077ffd76b2ac4bb5f1ea02c7be9e10a03a59456a8c0f04` |
| `RODADAS.md` | `d6fb060aaef7058dd310aa730460bed7e564557a00ec4695beb976496898db6a` |
| `RESUMO_SIMPLES.md` | `5cbcf64d7bcb36bdd80671cb017f516c35110dc1fb9e769355b7cf9f4eec2712` |

---

## 1. Os EUA

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Trump a repórteres em Joint Base Andrews (na CNN Brasil, também: *"a eleição pareceu tão corrupta"* e que não comanda o Brasil): a eleição pareceu *"like another rigged election"*; *"Elections have to be indisputable, and it looked very bad to me"*; *"I didn't take sides"* | 26/out | Euronews (`r2_01`), Al Jazeera (`r2_04`) | sim |
| Na mesma fala: *"The extension given was very strange"* | 26/out | Reuters via Yahoo (`r2_02`) | uma (as outras trazem o resto da fala) |
| Na mesma fala, em português: *"gosto do Lula"*, *"me dou muito bem com ele"* | 26/out | CNN Brasil (`r2_03`), SBT (`r2_07`) | sim |
| O Departamento de Estado tinha uma nota pronta e o governo *"determinou o adiamento da publicação para avaliar a situação política no Brasil"* | 26/out | Folha, via Tribuna do Norte (`r2_05`) e Estado de Minas (`r2_06`) | sim como reportagem, mas a origem é uma só (a Folha) |
| Alckmin: a fala do Trump é *"totalmente equivocada"*; o Planalto e o Itamaraty decidiram não reagir oficialmente | 26 e 27/out | SBT (`r2_07`), Reuters (`r2_02`: *"totally wrong"*) | sim |
| **Não encontrado:** nota da Casa Branca, do Departamento de Estado ou da embaixada; fala confirmada do Rubio (uma frase atribuída a ele no The Conversation não tem data, local nem outra fonte e fica fora); tarifa, sanção ou revogação de visto nova | até 27/out, 14h30 | · | · |

## 2. China, Rússia, Europa e América do Sul

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Xi Jinping mandou mensagem pessoal ao Lula; quer a parceria em *"novos patamares"* | 27/out (Reuters 7h40) | Metrópoles (`r2_09`), Carta Capital (`r2_10`); Reuters via Investing (`r2_08`, recusou leitura) | sim |
| Peskov, porta-voz do Kremlin: *"We welcome Mr. Lula's victory"* | 26/out | France 24 (`r2_13`) | uma |
| Macron, Modi, Sheinbaum, Carney e Pedro Sánchez deram os parabéns | 25 e 26/out | France 24 (`r2_13`), Al Jazeera (`r2_14`) | sim para Macron e Sheinbaum; Modi só na France 24 |
| Argentina, porta-voz Adrián Ravier: *"Tomamos nota do resultado eleitoral do Brasil"*, sem comunicado; Milei não falou | 27/out, 12h11 | CNN Brasil (`r2_11`), MDZ (`r2_12`) | sim |
| China e Rússia: nenhuma fala sobre interferência dos EUA, nem depois da fala do Trump | até 27/out | · | · |

## 3. C3 · a Justiça e a anulação

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Flávio desistiu do pedido de anulação: *"não haverá pedido de anulação da votação"* | 26/out, 18h08 | CNN Brasil (`r2_15`), Metrópoles (`r2_16`, *"zero chance"*) | sim |
| A campanha passou a pedir a cassação da chapa por abuso de poder: *"20 ações com pedidos de cassação já foram apresentadas"*; sem número de processo nem tribunal | 26/out | Metrópoles (`r2_16`), Poder360 (`r2_17`, AIJE em preparo) | sim como fala da campanha; protocolo não encontrado |
| O PL reconheceu o resultado em nota de Valdemar Costa Neto | 26/out | Al Jazeera (`r2_04`); Terra (`r2_18`, recusou leitura) | sim |
| Republicanos, MDB, União Brasil, PSD e PSDB reconhecem; Caiado: *"nos curvamos"*; Zema não reconhece | 25 e 26/out | Correio Braziliense (`r2_19`) | uma para o conjunto |
| Tarcísio reconhece, com críticas: *"Reconhecer o resultado não significa"* calar sobre os excessos | 27/out | Metrópoles (`r2_20`) | uma |
| Eduardo Bolsonaro, em vídeo em inglês, pede que governos estrangeiros não reconheçam a eleição | 26/out | Estado de Minas (`r2_21`), Observador (`r2_22`) | sim |
| Nunes Marques, do TSE: *"não houve nenhuma alteração"* do resultado vinda da prorrogação | 25/out | Tribuna de Jundiaí (`r2_31`) | uma |

**C3 hoje:** aponta L **provisório**. A anulação saiu de cena por decisão do próprio Flávio; as ações de cassação não foram julgadas e o prazo das ações eleitorais ainda corre.

## 4. C1 e C2 · as urnas (do projeto do vídeo 16)

- **C1, parte a:** 34.810 votos depois das 17h em 30.086 seções, 13 depois das 19h; mesmo que todos fossem do Lula, 0,79% da diferença. A CNN Brasil, com dados do TSE, dá cerca de 34 mil e, no 1º turno, 3.724.999 depois das 17h (`r2_30`). **Aponta L.**
- **C1, parte b:** não há medida direta de eleitores impedidos. O sinal indireto: a abstenção caiu 1,86 ponto entre os turnos e o comparecimento subiu em 80% dos municípios.
- **C2:** RDV igual ao boletim em 499.177 seções nos votos do Lula e do Flávio; log igual ao boletim em 99,7%. **Aponta L**, com o menor peso (emenda 6).

## 5. C4 e C5

- **C4:** a PF tem 1 inquérito (Sergipe) e diligências em 4 estados, sem conclusão; nada novo de 26/out à tarde ou de 27/out. A OEA prometeu um *"relatório preliminar"* do 2º turno, sem data (Exame, `r2_34`). **Sem dado.**
- **C5:** TSE, 389 votos em papel sem divergência (página do TSE de 25/out, 20h11, lida em imagem; o texto recusa leitura automática, `r2_32`); São Paulo, 33 urnas sem divergência (TRE-SP, `r2_33`, recusou leitura; citado na rodada 6 do projeto do vídeo 16). O consolidado das 27 UFs sai em até 30 dias. **Aponta L em parte.**

## 6. Fato novo, fora dos critérios: o passaporte do Flávio

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Moraes manda o Flávio entregar os passaportes em 24 horas e proíbe a saída do país, num inquérito sigiloso que apura *"lavagem de dinheiro e evasão de divisas"* (não é sobre a eleição) | 26/out, 17h49 | CNN Brasil (`r2_23`), Jovem Pan (`r2_28`) | sim |
| A PF cancela os passaportes comum e diplomático: *"O prazo terminou às 11h"* | 27/out, 12h12 | CNN Brasil (`r2_24`), Euronews PT (`r2_25`) | sim |
| Um aliado disse à Reuters que ele saiu para os EUA | 27/out | Times of Israel (`r2_26`, recusou leitura); Jovem Pan (`r2_28`) | como relato de aliado |
| O coordenador da campanha, Rogério Marinho: *"Não saiu"* | 27/out | Euronews PT (`r2_25`) | uma |
| A Argentina diz não ter registro de entrada dele: *"no record of Flávio Bolsonaro entering the Argentine Republic"* | 27/out | Buenos Aires Times (`r2_27`), Euronews PT (`r2_25`) | sim |
| Aliados dizem que ele vai pedir asilo e que *"O governo Donald Trump já foi avisado"* | 27/out, 14h04 | Metrópoles, coluna (`r2_29`) | **fonte única**, sem pedido visto |
| **Não encontrado:** chegada confirmada aos EUA, pedido de asilo, fala do governo dos EUA sobre ele, ordem de prisão, número do processo, posição oficial do governo brasileiro | até 27/out, 14h30 | · | · |

A suposição nova (S13) mede o que importa para este projeto: se o governo dos EUA anuncia asilo ou recusa entregá-lo ao Brasil. Ela entra na rodada 2, depois do fato, e por isso fica **fora da nota de Brier**.
