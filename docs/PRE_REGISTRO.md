# Pré-registro: o que esperar dos EUA, da China e da Rússia depois do 2º turno de 2026

**Escrito e publicado em 26/out/2026, por volta das 8h (horário de Brasília), no dia seguinte ao 2º turno, antes de qualquer coleta deste projeto.** Tudo que vier depois deste commit e mudar alguma regra entra na §13 (emendas), datado, dizendo se veio antes ou depois de ver o dado.

Análise feita pelo Claude (Anthropic), a pedido de Gabriel Alexandre, com o método descrito abaixo. O projeto é público para que qualquer pessoa refaça e conteste cada passo.

---

## 0. O que já era conhecido antes deste commit

Este pré-registro não nasce às cegas. Antes de escrevê-lo, a sondagem da manhã de 26/out leu o seguinte, e **nada disso conta como acerto ou erro das suposições da §8**:

| Fato | Fonte |
|---|---|
| Lula 51,79% × Flávio Bolsonaro 48,21% dos válidos (64.256.232 × 59.826.041 votos; diferença de 4.430.191) | ABC Mais; TSE via Time e NPR (51,8 × 48,2) |
| A diferença de 2026 é o dobro da de 2022 (2,14 milhões) e maior que a de 2014 (3,46 milhões) | conta feita nos arquivos do TSE do projeto `previsao-segundo-turno-2026` |
| Flávio anunciou que não reconhece e vai pedir a anulação, por causa da prorrogação da votação até 19h decidida pelo ministro Cristiano Zanin (STF) | Conjur, Common Dreams, Al Jazeera |
| As duas campanhas pediram mais tempo de votação (a do Lula por falta de ônibus; a do Flávio por chuva em SP, SC e PR) | Metrópoles, AP, Al Jazeera |
| A prorrogação valeu só para seções ainda abertas às 17h; houve seções já fechadas, urnas desligadas no Rio e eleitores que voltaram para casa | Al Jazeera, Latin Times, Brasil 61 |
| Falta de ônibus em Salvador (544 parados, ordem de prisão do secretário de mobilidade), ônibus com adesivo do PT retidos em SP, inquérito da PF em 7 estados, OEA acompanhando | Times Brasil, Terra, NC News, Latin Times |
| Trump antes da votação: *"we are watching"*; depois, duas versões (silêncio, pela Time; questionamento com *"manual do Joe Biden"*, pela EFE via Rio Times) | Al Jazeera, Time, Rio Times |
| Martin De Luca, advogado da Trump Media e da Rumble: *"manipulação descarada"*, *"ninguém vai reconhecer"*; Donald Trump Jr. compartilhou e criticou a prorrogação; Eduardo Bolsonaro e Paulo Figueiredo falaram em *"golpe"* | CNN Brasil, Exame, Metrópoles, Poder360, DCM |
| Reuters (24/out): dois funcionários do Departamento de Estado teriam liderado um esforço para devolver os Bolsonaro ao poder; o Departamento não comentou as medidas | Reuters via US News |
| China parabenizou pelo porta-voz da chancelaria (uma fonte); da Rússia, nada encontrado | resumo de agência; kremlin.ru (2022) |
| Parabenizaram: México, Canadá, França, Cazaquistão; Milei em silêncio | Time, ICL, Qazinform |

Os links completos estão no plano, no repositório de documentação do autor (`contexto/projetos-externos/GEOPOLITICA_ELEICAO_2026_PLANO.md`), e serão capturados com hash em `dados/capturas/` na primeira fase.

---

## 1. As perguntas

| # | Pergunta |
|---|---|
| P1 | A contestação interna tem força para mudar alguma coisa? |
| P2 | Os EUA vão reconhecer o resultado? Separado em reconhecimento **formal** (continuar tratando o governo Lula como o governo do Brasil) e **político** (parabéns, nota, presença na posse, ou silêncio e questionamento) |
| P3 | O que os EUA podem fazer além de reconhecer ou não |
| P4 | O que esperar da China |
| P5 | O que esperar da Rússia |
| P6 | Os outros que pesam no reconhecimento (União Europeia, América Latina, Índia e África do Sul, observadores) |
| P7 | O que isso sugere para o Brasil até a posse (05/jan/2027) e no 1º ano do mandato |

---

## 2. As duas lentes

Toda pergunta roda pelas duas premissas, cada uma dada como verdadeira por vez, com a mesma régua.

| Lente | Definição |
|---|---|
| **L · legítimo, com as margens de dúvida** | o resultado reflete a vontade do eleitor; os problemas de procedimento (prorrogação desigual, falta de ônibus, pausa, falta de luz) são reais e não mudaram quem ganhou |
| **F1 · fraude demonstrada** | o resultado não reflete a vontade do eleitor, e isso fica demonstrado por prova pública aceita pela Justiça brasileira ou por observadores |
| **F2 · fraude não demonstrada** | o resultado não reflete a vontade do eleitor, mas a prova não aparece: boletins, logs e totalização fecham entre si |

⚠️ **F2 não é testável por dado, por definição**: é o mundo em que tudo o que se pode medir fecha. O projeto diz isso com essas palavras, e diz o que precisaria ser verdade para F2 existir (que mecanismo deixaria boletins, logs, totalização e o teste de integridade das urnas coerentes) e qual auditoria o exporia.

🔁 Dentro de cada lente, procura-se ativamente o que a derrubaria. E o espelho vale nas duas direções: a queixa da falta de ônibus é a versão mais forte de uma *"fraude a favor do Flávio"* e passa pela mesma régua.

---

## 3. Os critérios do peso de cada lente (fixados agora, antes do dado)

| # | Critério | Aponta L | Aponta F | Fonte |
|---|---|---|---|---|
| C1 | **Teto da prorrogação:** votos registrados depois das 17h no 2º turno, acima da fila normal medida nas mesmas seções no 1º turno, no pior caso (todos de um lado só) | o teto fica abaixo de 4.430.191 | o teto alcança a diferença **e** os votos depois das 17h divergem do perfil das mesmas seções no 1º turno além do que o perfil de quem vota tarde explica | projeto `apuracao-segundo-turno-2026` (vídeo 16), copiado com hash; se não existir, refeito aqui com os logs das urnas |
| C2 | **Integridade da contagem:** soma dos boletins de urna contra a totalização, e logs contra boletins | diferença nula ou imaterial | diferença capaz de mudar 4.430.191 votos | mesmo projeto, ou os arquivos do TSE |
| C3 | **Justiça:** a ação de anulação | julgada improcedente ou não proposta | julgada procedente, com anulação ou nova votação | TSE e STF |
| C4 | **Inquéritos e observação:** inquérito da PF sobre transporte, relatórios da OEA e de outras missões | sem irregularidade capaz de mudar o resultado | irregularidade comprovada capaz de mudar o resultado | relatórios públicos |
| C5 | **Teste de integridade das urnas** (votação paralela do dia da eleição) | resultados batendo | divergência entre o votado e o registrado | TSE |

**Veredito de lente:** *L sustentada* quando C1 e C2 apontam L e nenhum critério aponta F. *F1* quando C2, C3 ou C5 apontam F. Fora disso, *aberta*, com o porquê. Critério sem dado na data do relatório aparece como *sem dado*, e o veredito diz isso.

---

## 4. A escala de probabilidade

Escala da norma de análise da comunidade de inteligência dos EUA (ICD 203, 2015), com o ponto do meio usado na nota de Brier:

| Palavra | Faixa | Ponto usado |
|---|---|---|
| quase nenhuma chance | 1 a 5% | 3% |
| muito improvável | 5 a 20% | 12,5% |
| improvável | 20 a 45% | 32,5% |
| chance parecida | 45 a 55% | 50% |
| provável | 55 a 80% | 67,5% |
| muito provável | 80 a 95% | 87,5% |
| quase certo | 95 a 99% | 97% |

---

## 5. A classe de referência (o histórico)

**Regra de entrada:** eleição nacional que define o governo, de 1990 a 2026, em que (a) o perdedor ou parte relevante não aceitou o resultado, **ou** (b) EUA, China, Rússia ou a União Europeia demoraram, condicionaram ou negaram o reconhecimento.

**Base sistemática:** NELDA (*National Elections Across Democracy and Autocracy*, Hyde e Marinov) para a taxa-base de protesto depois da eleição, crítica de governos ocidentais e posição de observadores. Casos posteriores ao fim da base entram codificados à mão com a mesma ficha.

**Casos com ficha completa:** Brasil 2014, 2018 e 2022; EUA 2000 e 2020; México 2006; Peru 2021; Quênia 2007 e 2017; Malaui 2019; Romênia 2024; Venezuela 2013, 2018 e 2024; Nicarágua 2021; Bielorrússia 2020; Bolívia 2019; Ucrânia 2004; Sérvia 2000; Geórgia 2003; Costa do Marfim 2010; Honduras 2017 e 2025; Hungria 2026; Argentina 2025. Caso que não fechar com duas fontes sai da conta, e a saída é registrada.

**A ficha:** a fraude foi demonstrada, por quem e com que prova? a autoridade eleitoral certificou? os observadores validaram? margem? o perdedor foi à Justiça? havia governo ou candidato paralelo reconhecido por alguém? relação do vencedor com Washington, Pequim e Moscou? tempo até os parabéns de cada potência? sanção, tarifa ou corte de ajuda? quem tomou posse? houve violência?

**Codificação:** duas passadas independentes, com a concordância medida (kappa de Cohen); divergência resolvida por regra escrita, não por escolha.

---

## 6. As hipóteses concorrentes

| Potência | Hipótese | Previsão |
|---|---|---|
| EUA | H1 · Institucional: seguem a certificação local e os observadores | nota reconhecendo em poucos dias, delegação na posse |
| EUA | H2 · Alinhamento: a reação depende de quem ganhou | silêncio ou frieza, questionamento retórico sem ato formal |
| EUA | H3 · Troca: o reconhecimento político vira moeda numa negociação | aproximação com condição anunciada |
| EUA | H4 · Contestação ativa: apoiam a anulação | declaração oficial de fraude, sanção ligada à eleição |
| China | H5 · Segue a autoridade eleitoral do país | parabéns logo depois da proclamação |
| China | H6 · Aproveita a fricção com os EUA | oferta de acordo ou crítica pública à interferência |
| Rússia | H7 · Segue a autoridade eleitoral do país | telegrama de Putin |
| Rússia | H8 · Usa o caso contra os EUA | fala da chancelaria sobre interferência americana |
| Círculo | H9 · As falas de quem fala pelo círculo do Trump (advogado, filho, aliados com acesso) antecipam a posição oficial | medido em Honduras 2025, Hungria 2026, Argentina 2025 e nas medidas contra o Brasil em 2025: quantas falas do círculo viraram ato oficial em até 60 dias |

Vence, em cada potência, a hipótese com **menos evidência contra** (análise de hipóteses concorrentes, Heuer, 1999).

---

## 7. O método, em uma linha por peça

Taxa-base primeiro e ajuste pelo caso depois (Tetlock); hipóteses concorrentes (Heuer); probabilidade com a escala da §4; indicadores datados com critério de resolução (§8); nota de Brier no teste do passado e na conferência das suposições.

---

## 8. A primeira leitura (as suposições, antes dos dados)

Cada linha tem a faixa nas três lentes e o **critério de resolução**. A nota de Brier é calculada com a coluna da lente que o veredito da §3 apontar; com o veredito *aberta*, as duas notas são publicadas.

| # | Suposição | L | F1 | F2 | Resolve **sim** se | Prazo |
|---|---|---|---|---|---|---|
| S1 | A Justiça brasileira anula ou manda refazer o 2º turno | quase nenhuma chance | provável | quase nenhuma chance | decisão do TSE ou do STF anulando o 2º turno ou mandando nova votação | 05/jan/2027 |
| S2 | Lula toma posse | quase certo | improvável | quase certo | posse em 05/jan/2027 | 05/jan/2027 |
| S3 | Há protestos de rua contra o resultado | provável | quase certo | provável | bloqueios ou atos contra o resultado em pelo menos 5 estados, noticiados por 2 veículos nacionais | 25/nov/2026 |
| S4 | Os EUA continuam tratando o governo Lula como o governo do Brasil | quase certo | improvável | quase certo | resolve **não** se os EUA reconhecerem outra pessoa como presidente ou romperem relações | 31/dez/2027 |
| S5 | Trump parabeniza Lula em público | muito improvável | quase nenhuma chance | muito improvável | mensagem do próprio Trump (fala, post ou carta) cumprimentando Lula pela vitória | 25/nov/2026 |
| S6 | O Departamento de Estado trata o resultado como válido em público | chance parecida | quase nenhuma chance | chance parecida | nota, fala do secretário ou do porta-voz chamando Lula de vencedor, reeleito ou presidente eleito, ou pedindo respeito ao resultado | 25/nov/2026 |
| S7 | Trump ou o governo dos EUA dizem em público que houve fraude, ou apoiam a anulação | improvável | muito provável | improvável | fala do Trump, da Casa Branca, do Departamento de Estado ou do Tesouro dizendo que a eleição foi fraudada, roubada ou manipulada, ou apoiando a anulação. Falas do círculo (§6, H9) **não** contam | 05/jan/2027 |
| S8 | Os EUA adotam nova medida contra autoridades ou contra a economia brasileira | provável | quase certo | provável | nova designação da OFAC de autoridade brasileira, nova tarifa contra o Brasil, ou revogação de visto de autoridade brasileira anunciada pelo governo dos EUA | 05/jan/2027 |
| S9 | Xi Jinping manda mensagem pessoal a Lula | muito provável | improvável | muito provável | mensagem assinada por Xi, publicada pela chancelaria chinesa ou pela Xinhua | 02/nov/2026 |
| S10 | Putin parabeniza Lula | muito provável | improvável | muito provável | mensagem de Putin publicada no kremlin.ru | 02/nov/2026 |
| S11 | China ou Rússia citam em público interferência dos EUA na eleição brasileira | chance parecida | improvável | chance parecida | porta-voz ou ministro das chancelarias dizendo que os EUA interferiram | 25/nov/2026 |
| S12 | No 4º mandato o Brasil fica mais perto da China do que dos EUA | provável | não se aplica | provável | em 2027, a diferença China menos EUA cresce contra 2025 **nos dois** indicadores: fatia das exportações brasileiras e concordância nos votos da Assembleia Geral da ONU | 31/dez/2027 |

**Porquê de cada faixa:** no plano do autor, §9. Em uma linha: o reconhecimento formal só cai em F1; em L e F2 a dúvida é o reconhecimento político, e as falas do círculo do Trump puxam S5 a S8 para frieza e pressão (consistente com H2 e H3); China e Rússia seguem a autoridade eleitoral nas duas lentes. **F2 repete L** porque governo estrangeiro reage ao que dá para mostrar.

**Leitura da lente, hoje:** o dado conhecido antes deste commit sustenta mais a L (diferença o dobro da de 2022, as duas campanhas pediram mais tempo, problemas de procedimento apontando para os dois lados, nenhuma prova de voto alterado nas fontes lidas). Isso **não** é o veredito: o veredito sai dos critérios da §3.

---

## 9. Dados e fontes

- Reações oficiais: whitehouse.gov, state.gov, Truth Social, fmprc.gov.cn, kremlin.ru, mid.ru, gov.br/mre, Conselho Europeu e chancelarias da América do Sul. Captura em até 72 h, 7 dias e na posse.
- Falas do círculo do Trump e do círculo do Lula: postagens e entrevistas, com o vínculo como a fonte o descreve.
- Comércio: Comex Stat (MDIC). Investimento: Banco Central. Minerais críticos: USGS, *Mineral Commodity Summaries 2026*. Sanções: lista da OFAC. Tarifas: Registro Federal dos EUA e USTR. Votos na ONU: base de Erik Voeten (Harvard Dataverse).
- Contestação: processos no TSE e no STF; inquérito da PF; relatórios de observação; resultados do teste de integridade das urnas.
- Toda captura com endereço, hora e sha256 em `dados/MANIFESTO.json`. ⛔ No git entra o texto extraído, nunca o HTML bruto. ⛔ Resumo automático de página não é fonte: todo número é conferido no texto capturado.

---

## 10. Validação

- **Dois caminhos:** os números centrais (comércio, votos na ONU, tempos até os parabéns) refeitos por script independente.
- **Revisão adversarial:** três leitores, um que defende a lente F, um que defende a L e um auditor de método e linguagem; a objeção mais forte de cada lado vira variante calculada e publicada.
- **Teste do passado:** o método aplicado a Brasil 2022, Honduras 2025 e Hungria 2026 só com o que se sabia na noite do resultado; nota de Brier de cada um, publicada como sair.

---

## 11. Linguagem e travas

- *"Fraude"* aparece só como hipótese das lentes F1 e F2, dita como hipótese, ou entre aspas, na boca de quem disse. O projeto não afirma nem nega fraude fora do veredito da §3, e o mesmo vale para *"legítimo"*.
- Não se julga intenção de pessoa; mede-se ato e declaração (*"a medida é consistente com"*).
- Sem recomendação de voto ou de posição política.
- Reportagem com fonte anônima entra como *"segundo a Reuters"*, nunca como fato do projeto.
- Os dois lados de cada fato entram juntos (a apuração da Reuters e a negativa do Departamento de Estado; os pedidos de prorrogação das duas campanhas).

---

## 12. O que o projeto não faz

- Não decide se houve fraude por opinião: o peso das lentes sai dos critérios da §3, e F2 é declarada não testável.
- Não prevê destino: as suposições são probabilidades com prazo e critério de resolução.
- Não refaz a apuração: a contagem e a prorrogação são do projeto `apuracao-segundo-turno-2026`.

---

## 13. Emendas

Nenhuma até agora.
