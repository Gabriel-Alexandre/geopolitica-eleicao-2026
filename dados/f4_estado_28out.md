# Rodada 3 · o estado dos critérios e das reações em 28/out/2026

**Busca feita em 28/out/2026, das 16h às 18h (horário de Brasília), cobrindo o que saiu depois da rodada 2 (27/out, 14h30).** Cada citação abaixo está em `dados/citacoes_r3.csv` e foi conferida palavra por palavra no texto capturado com sha256 (`dados/capturas/r3_*.txt`, registro em `dados/MANIFESTO.json`; o teste `test_rodada_3_toda_citacao_esta_no_texto_capturado_com_hash` refaz a conferência). Das 58 fontes da lista `dados/fontes_r3.csv`, 52 foram capturadas; as que recusaram leitura (HTTP 403 ou 404) ficam marcadas e nenhuma sustenta fato sozinha. O relatório da OEA é PDF e foi lido por `ferramentas/capturar_pdf.py`.

A curva oficial da noite (as 346 versões do resultado publicadas pelo TSE) vem do projeto público do vídeo 16, `investigacao-segundo-turno-2026` (commit `d706893`), copiada com sha256 para `dados/derivados/video16/`:

| Arquivo copiado | sha256 |
|---|---|
| `d5_curva_noite.csv` | `983557aa491f7c3752f30d3395b5c38f56c864f9f89df844abec6ec43af95e5f` |

---

## 1. A hora do pedido do passaporte (a pergunta dos *"7 minutos"*)

| Fato | Hora | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| A Polícia Federal assinou a representação de 16 páginas pedindo a apreensão dos passaportes | 25/out, **21h16** (assinatura digital) | Estado de Minas (`r3_01`), O Antagonista (`r3_23`), Revista Fórum (`r3_24`), DCM (`r3_25`), Pleno News (`r3_26`); todas citam uma coluna de *O Globo* (Bela Megale, segundo o Estado de Minas; Malu Gaspar, segundo o Pleno News) | sim como reportagem, mas a origem é uma só (O Globo); a nota oficial da PF confirma o dia, 25/out, sem a hora (`r3_33`) |
| O sistema do TSE confirmou o resultado matematicamente | 25/out, **21h09** | Estado de Minas (`r3_01`), Revista Fórum (`r3_24`), DCM (`r3_25`) | sim, mesma origem; conferido na curva oficial: a versão de **21h08min21s** (96,83% das seções) é a 1ª em que a vantagem do Lula (4.176.278 votos) passa a estimativa dos votos que faltavam (3.926.293, proporcional às seções); a de 21h09min01s tinha 97,69% |
| A apuração chegou a 100% das seções | 25/out, **23h26** (OEA) · 23h27min02s (última versão do arquivo oficial) | relatório preliminar da OEA (`r3_58`), curva oficial (`d5_curva_noite.csv`) | sim |
| O Moraes atendeu ao pedido | 25/out, **"no domingo à noite"**, sem consultar a PGR; **a hora não foi divulgada**: *"o STF não esclareceu o horário de assinatura da decisão sigilosa do relator"* | Estado de Minas (`r3_01`), Gazeta do Povo (`r3_02`), InfoMoney (`r3_11`, versão do Flávio) | sim para "domingo à noite"; a hora, nenhuma fonte |
| A versão do coordenador da campanha, Rogério Marinho: *"Às 20h44 é proclamado o resultado. Sete minutos depois, a Polícia Federal requer medidas cautelares"* | 27/out | Gazeta do Povo (`r3_02`) | uma; **a conta não fecha**: 20h44 mais 7 minutos dá 20h51, não 21h16. O Datafolha projetou a reeleição às 20h46 (DCM, `r3_25`) |

**Leitura:** os 7 minutos separam a confirmação matemática do TSE (21h09) da **assinatura do pedido da Polícia Federal** (21h16), não da decisão do Moraes, cuja hora o STF não informou. O pedido foi assinado **2 horas e 10 minutos antes** de a apuração chegar a 100% (23h26). Frase segura: *"o pedido da Polícia Federal foi assinado 7 minutos depois de o TSE confirmar matematicamente a vitória do Lula, e o Moraes atendeu na mesma noite; o STF não informou a hora da decisão"*.

## 2. O Flávio

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| A migração argentina revisou o que tinha dito: o Flávio, a mulher e as 2 filhas entraram pela Ponte Tancredo Neves às **22h50** de 27/out, *"with valid travel documents"*, e às 23h30 embarcaram num avião particular da Baires Fly para Guayaquil, no Equador | 27/out à noite (nota na madrugada de 28/out) | Metrópoles (`r3_04`), Reuters via Yahoo (`r3_16`), CNN en Español (`r3_50`) | sim |
| Desembarcou com a família no aeroporto executivo de Opa-Locka, em Miami | 28/out, **por volta das 10h25** (Brasília) | Metrópoles (`r3_04`, `r3_05`), Gazeta do Povo (`r3_40`) | sim |
| Entrou nos EUA na categoria **"DT"** (*parole*, permissão de entrada temporária, que pode ser humanitária), válida até 27/out/2027; não é asilo | 28/out | Metrópoles, coluna de Igor Gadelha, com registros da alfândega (`r3_30`); repetido por Revista Fórum (`r3_31`), Folha BV (`r3_32`) e um blog (`r3_07`) | **origem única** (Metrópoles) |
| Na Argentina teria usado o passaporte italiano (segundo o El País, citado no Brasil) | 27/out | Metrópoles (`r3_05`), InfoMoney (`r3_19`), Revista Fórum (`r3_31`) | como relato de imprensa |
| Carta divulgada por aliados (Paulo Figueiredo): *"eu sou o presidente eleito e os criminosos que roubaram a eleição do Brasil"* […]; *"não fugi do Brasil, eu saí pelo Brasil"*; agradece ao Trump e ao Milei | 28/out, à tarde | O Antagonista (`r3_42`), Gazeta do Povo (`r3_40`), Jornal Opção (`r3_47`), Metrópoles (`r3_41`) | sim |
| Nota da Polícia Federal: representou ao STF *"no dia 25 de outubro"*; a restrição de documento *"não caracteriza a condição de foragido nem autoriza a realização de prisão"*; não há registro oficial de saída pelos postos brasileiros; investiga o descumprimento | 28/out, 14h48 | Poder360 (`r3_33`) | uma (é a nota oficial; Gazeta do Povo cita a mesma nota em manchete) |
| A PF *"considera solicitar sua prisão preventiva"* e o bloqueio de bens | 28/out | Diário Carioca (`r3_34`), DCM (`r3_35`) | sim como reportagem; **nenhum pedido nem decisão** encontrados |
| **Não encontrado:** mandado de prisão, pedido de extradição, pedido de asilo protocolado, difusão vermelha da Interpol | até 28/out, 18h | · | · |

## 3. Os EUA

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Um alto funcionário do Departamento de Estado: *"the State Department will issue visas to Flávio Bolsonaro and his family and allow them entry into the United States"*; não disse nada sobre asilo | 27/out (terça) | AP via PBS (`r3_14`), Reuters via Yahoo (`r3_16`), Al Jazeera (`r3_13`), Fox News (`r3_15`) | sim |
| Trump a repórteres, sobre a entrada do Flávio: *"Eu aprovaria. Acho que são boas pessoas."*; e *"The election was very strange, and I thought it was terrible"*; repetiu que não tomou partido | 27/out, à noite | Reuters via Yahoo (`r3_16`), Metrópoles (`r3_04`) | sim |
| O deputado democrata Joaquin Castro: *"Losing an election is not grounds for asylum."* | 27/out | Al Jazeera (`r3_13`) | uma |
| **Não encontrado:** nota do Departamento de Estado ou da Casa Branca sobre o resultado da eleição; o Trump dizendo que a eleição *foi* fraudada (sem o *"pareceu"*); tarifa, sanção ou revogação de visto nova contra o Brasil | até 28/out, 18h | · | · |

## 4. O círculo do Trump

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Martin De Luca, em entrevista à Gazeta do Povo (coluna Entrelinhas e programa Sem Rodeios): pede investigação independente da prorrogação; *"a alternativa seria simplesmente aceitar refazer o segundo turno"*; e *"Se o Lula ganhou, de fato, por 4 milhões de votos, eu vou ser o primeiro a falar que, absolutamente, vai ter que reconhecê-lo"* | 26/out, 17h47 | Gazeta do Povo (`r3_38`); a entrevista em vídeo e a da CNN Brasil estão transcritas na ficha do vídeo 17, fora deste repositório | texto e vídeo do mesmo veículo |
| De Luca no X, sobre a saída do Flávio: *"esta postagem envelheceu bem"* | 27/out | ND Mais (`r3_39`) | uma |
| Steve Bannon, no War Room: *"Rompam as relações diplomáticas. Interrompam tudo com o Brasil."* | 26/out | Gazeta do Povo (`r3_46`) | uma |

## 5. O resto do mundo e o Brasil

| Fato | Quando | Fonte (captura) | 2 fontes? |
|---|---|---|---|
| Lula sobre a saída: *"The act of leaving Brazil is shameful."* | 27/out | Al Jazeera (`r3_13`), Reuters (`r3_16`, em paráfrase) | sim |
| Itamaraty: fontes dizem que *"o caso deve ser tratado na esfera judicial"* e evitam reagir ao Trump | 28/out, 12h17 | CNN Brasil (`r3_43`) | uma |
| Argentina: a Casa Rosada não vai reconhecer o resultado por enquanto, segundo fontes ao La Nación; o Milei é o único presidente sul-americano sem reconhecer; a passagem do Flávio ampliou a crise com o Brasil | 27 e 28/out | Latin Times (`r3_51`), Gazeta do Povo (`r3_49`) | sim para a crise; o *"único"* é de uma fonte |
| Flávio Dino, do STF, mandou a PF investigar suspeita de **interferência estrangeira** na eleição (financiamento externo, publicidade paga de fora, plataformas) | 27/out | Correio Braziliense (`r3_56`), InfoMoney (`r3_57`) | sim |
| China e Rússia: nada novo depois da rodada 2; nenhuma fala sobre a saída do Flávio ou sobre interferência dos EUA | até 28/out | · | · |

## 6. Os critérios

- **C4 · ganhou dado:** a missão da OEA publicou o relatório preliminar do 2º turno em 27/out: os resultados do TSE *"coincidem com as informações coletadas em campo"* e *"a MOE/OEA não tem dúvidas quanto à integridade dos dados oficiais"* (PDF da OEA, `r3_58`; SBT News, `r3_48`). O inquérito da PF sobre a falta de ônibus segue sem conclusão. **Aponta L em parte.**
- **C3:** nenhuma ação de cassação julgada; nenhum número de processo das ações anunciadas depois do 2º turno (a AIJE sobre o Ministério da Cultura, distribuída em 28/set, é de antes da votação, `r3_52`). A carta do Flávio volta a falar em eleição roubada, mas é fala, não ação. **Segue L provisório.**
- **C5:** o consolidado das 27 UFs ainda não saiu. **Segue L em parte.**
- **C1 e C2:** sem mudança.

**Veredito de lente:** continua *L na frente, sem prova para nenhum lado*, agora com os 5 critérios apontando L, 3 deles com ressalva (C3 provisório, C4 e C5 parciais).
