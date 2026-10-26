# Revisão adversarial: o auditor de método e linguagem

**26/out/2026.** Leitor sem lado. Li o pré-registro com as emendas 1 a 3, o `RELATORIO.md`, o `RESUMO_SIMPLES.md`, `docs/LEITURA_DA_IA.md`, `docs/F1_REACOES.md`, `docs/F4_CONTESTACAO.md`, `dados/f4_estado_26out.md`, os scripts de `ferramentas/`, `resultados/RESUMO.json`, `resultados/f2_*.csv`, `resultados/f6_teste_do_passado.csv`, `resultados/validacao_independente.csv`, `dados/MANIFESTO.json` e `dados/MANIFESTO_F3.json`. Refiz os números a partir das passadas brutas (`dados/casos/`), dos arquivos do Comtrade e do Voeten em `dados/brutos/` e do texto capturado do USGS, com um script meu que não importa nenhum script do projeto. Rodei `python ferramentas/conferir_linguagem.py` (0 achados) e `python -m pytest -q` (4 testes passam).

**Resumo em três linhas.** A aritmética está certa: 9 dos 10 números refeitos batem, e o que não bate é um arredondamento do kappa. Os problemas estão na regra e na palavra: a manchete *"2 de 5 critérios apontam L"* contradiz o próprio levantamento da F4, a lente F do histórico mistura fraude demonstrada com disputada sem emenda, e a justificativa da S8 diz *"nenhuma eleição da lente L teve sanção"* enquanto o caso de Honduras 2025 está fora da conta exatamente por divergir nesse campo. O teste do passado não vaza o caso testado, e o condicionamento na relação do vencedor ajuda contra uma referência mais dura que o chute de 50%.

---

## 1. Achados

Gravidade: **alta** muda uma conclusão publicada ou contradiz uma regra escrita; **média** enfraquece uma conclusão ou deixa regra sem emenda; **baixa** é forma, precisão ou clareza.

| # | Achado | Onde | Gravidade | Conserto proposto |
|---|---|---|---|---|
| 1 | **C3 aparece como "aponta L (provisório)" no relatório, mas o levantamento que o sustenta diz *sem dado*.** O `dados/f4_estado_26out.md` §1 escreve: *"C3 hoje: sem dado (ação não proposta até 10h05) [...] o critério fica aberto"*. O `dados/criterios_c1_c5.csv` marca `L_provisorio`, e daí sai a manchete *"2 de 5 critérios apontam L"* no relatório, no resumo e na F4. A §3 diz *"não proposta"*, mas a ação foi anunciada na véspera e o prazo está aberto; e o único sinal a mais é fonte anônima (*"ministros ouvidos em reserva"*), que a §11 manda tratar como *"segundo o g1"*, não como estado de critério | `dados/criterios_c1_c5.csv`; `RELATORIO.md` §1 e §3; `RESUMO_SIMPLES.md`; `docs/F4_CONTESTACAO.md` | alta | C3 = *sem dado*, como diz o F4. Manchete: *"nenhum critério resolvido; nenhum aponta F; C5 com sinal parcial na direção de L; C1 a C4 sem dado"*. O veredito (*aberta*) não muda; muda a frase que o acompanha |
| 2 | **C5 usa número que a regra do próprio projeto não aceita.** Os *389 votos* do TSE vêm só do *resumo de busca* (página com HTTP 403), e o F4 diz que resumo de busca *"não é fonte de número"*; o caso do DF tem uma fonte só (*"conferido em duas fontes: não"*). O relatório publica *"sem divergência no TSE (389 votos)"* sem esse aviso | `dados/f4_estado_26out.md` §3; `RELATORIO.md` §3 | média | Tirar o 389 até capturar o texto da página do TSE, ou capturá-lo com hash; marcar o DF como fonte única; C5 fica *parcial, sem fonte dupla* |
| 3 | **A lente F do histórico junta `sim` e `disputado` sem emenda.** O pré-registro define F1 como fraude **demonstrada** por prova aceita pela Justiça ou por observadores. Na conta, a coluna *"lente F"* tem 6 casos: 2 `sim` (Bielorrússia 2020, Venezuela 2024) e 4 `disputado`. As 3 anulações da lente F (Bolívia 2019, Quênia 2017, Romênia 2024) são **todas** `disputado`; nos 2 casos `sim`, 0 de 2 anulados e 2 de 2 com posse. A justificativa da S1 em F1 (*"com fraude demonstrada ou disputada, metade foi"*) apoia uma faixa de F1 em casos que não são F1. A Romênia 2024 foi anulada por interferência na campanha, não por voto alterado | `ferramentas/analise.py` (`grupos_lente`); `RELATORIO.md` §1 (S1, S2) e §4 | alta | Emenda 4, dita como escrita **depois** de ver o dado, explicando o agrupamento; publicar as duas tabelas (só `sim`, e `sim` mais `disputado`); reescrever o porquê da S1 e da S2 em F1 sem apoiar a faixa nas anulações dos casos disputados |
| 4 | **S8: a justificativa contradiz a ficha.** O texto diz *"no histórico nenhuma eleição da lente L teve sanção dos EUA ligada a ela"* e, na mesma linha, *"restringiu vistos em Honduras"*. Honduras 2025 é lente L e está fora do *"0 de 9"* porque as passadas divergem justamente nesse campo (passada A: `true`; passada B: `false`). O critério da S8 conta revogação de visto como medida. Com Honduras 2025 contado como sanção, a lente L fica 1 de 10 | `RELATORIO.md` §1 (S8); `docs/LEITURA_DA_IA.md` S8; `resultados/f2_casos_consenso.json` | alta | Dizer *"0 de 9, com Honduras 2025 fora por divergência entre as passadas, e a passada A marca restrição de visto"*; publicar a variante 1 de 10; reavaliar se a S8 ainda *"desceu"* com esse fato na frente |
| 5 | **As faixas mudaram depois do dado (S7, S8, S9, S11) e não está escrito qual coluna entra na nota de Brier.** A §8 diz que a nota usa *"a coluna da lente que o veredito apontar"*, sem dizer se é a do pré-registro ou a final. S7 e S8 foram para *chance parecida*, que é o ponto que menos perde na nota de Brier | `RELATORIO.md` §1; `dados/sintese_suposicoes.csv` | média | Emenda: a nota oficial usa as colunas `pre_*`; as colunas `final_*` têm nota publicada à parte, lado a lado |
| 6 | **A fonte do comércio mudou sem emenda.** A §9 diz Comex Stat (MDIC); o projeto usou UN Comtrade. O motivo (a API do Comex Stat respondeu 429) está só no cabeçalho de `coletar_f3.py` | `ferramentas/coletar_f3.py`; `docs/PRE_REGISTRO.md` §9 | média | Emenda 4 registrando a troca e o motivo; idealmente, conferir 2025 no Comex Stat quando a API voltar |
| 7 | **A NELDA, base sistemática da §5, não foi usada.** A taxa-base saiu só dos 25 casos codificados à mão | `docs/PRE_REGISTRO.md` §5 | média | Emenda dizendo que a NELDA ficou fora e por quê, ou rodar a taxa de protesto e de crítica ocidental na NELDA como variante |
| 8 | **H9 pede uma contagem e o relatório entrega narrativa.** O pré-registro: *"quantas falas do círculo viraram ato oficial em até 60 dias"* em Honduras 2025, Hungria 2026, Argentina 2025 e nas medidas de 2025. O relatório conta dois episódios | `RELATORIO.md` §6; `dados/hipoteses_veredito.csv` | média | Tabela fala por fala (quem, data, ato oficial em 60 dias sim ou não), com o total |
| 9 | **A regra de decisão da §6 (vence a hipótese com menos evidência contra) não foi aplicada por escrito.** Para os EUA, H3 tem zero evidência contra e é listada depois da H2 | `RELATORIO.md` §6 | baixa | Matriz de Heuer com a contagem de evidência contra por hipótese; com empate, dizer empate |
| 10 | **A captura em 7 dias e na posse, prevista na §9, virou opcional** (*"se o autor quiser"*) | `ESTADO.md` | baixa | Manter como etapa, ou emenda dizendo que sai |
| 11 | **A revisão adversarial está marcada como feita e o arquivo não existe.** O relatório linka `docs/REVISAO_ADVERSARIAL.md`; o `ESTADO.md` marca F7 com ✅. A §10 pede que a objeção mais forte de cada lado vire variante calculada e publicada | `RELATORIO.md` §7; `ESTADO.md` | média | Juntar as três revisões nesse arquivo, calcular as variantes e só então marcar F7 |
| 12 | **O deixa-um-de-fora usa casos posteriores ao caso testado.** Brasil 2014 é previsto com Hungria 2026 dentro da conta. Não vaza o desfecho do próprio caso, mas não é *"só com o que se sabia na noite"* da §10. A emenda 2 escreve *"taxa-base dos outros casos"*, então a regra foi seguida; a frase do relatório é que promete mais | `ferramentas/analise.py` (`teste_do_passado`); `RELATORIO.md` §4 | média | Publicar a variante só com casos anteriores (Brier 0,214, seção 3) e trocar a frase do relatório por *"cada caso previsto pelos outros"* |
| 13 | **A comparação com o chute de 50% é a mais fácil possível, e as 145 previsões não são independentes.** Vários desfechos têm taxa longe de 50% (posse, anulação), então qualquer taxa-base ganha do 50%. `eua_parabens_30d` e `eua_nao_reconheceu` saem do mesmo campo. E o teste mede a taxa-base, não as faixas finais que a IA ajustou | `RELATORIO.md` §4; `resultados/RESUMO.json` | média | Publicar as três referências (seção 3) e a frase: *"o teste mede a taxa-base condicionada, não as faixas finais das suposições"* |
| 14 | **A suavização de Laplace ((sim+1)/(n+2)) não está em nenhuma emenda** | `ferramentas/analise.py` | baixa | Uma linha na emenda que registrar a seção 3 |
| 15 | **Kappa mediano publicado como 0,93; a mediana dos 16 kappas é 0,92** (0,914 e 0,925). O script pega o elemento de cima. E o campo `autoridade_certificou_o_resultado_anunciado` tem 96% de concordância com kappa 0,0 (quase tudo `true`), que a média esconde | `ferramentas/analise.py` (`kappa_mediano`); `RELATORIO.md` §4 | baixa | Usar a mediana de verdade; citar o kappa 0,0 com a explicação (prevalência alta) |
| 16 | **F1 diz "Captura: 49 de 42 páginas".** O certo é 39 de 42: o `gerar_f1.py` conta todas as entradas `ok` do `MANIFESTO.json`, que passou a ter também `m01` a `m10` da F3 | `docs/F1_REACOES.md`; `ferramentas/gerar_f1.py` | média | Contar só os ids de `dados/fontes_f1.csv` |
| 17 | **3 casos somem das tabelas por lente sem aviso.** Malaui 2019, Venezuela 2018 e Nicarágua 2021 divergem em `fraude_demonstrada` e não entram em nenhuma das duas colunas; a tabela por lente tem no máximo 16 casos, não 19. Por isso o leitor vê *"não reconheceram: 0 de 8 e 2 de 5"* e, noutro lugar, *"4 de 5 com vencedor adversário"* | `RELATORIO.md` §4; `docs/LEITURA_DA_IA.md` S4 | média | Nota abaixo da tabela com os 3 casos e o motivo |
| 18 | **"Votou igual à China em 80% das votações"** lê o índice `agree` do Voeten como porcentagem de votos iguais. O índice dá peso parcial à abstenção (conferir no codebook do conjunto) | `RELATORIO.md` §5; `ferramentas/gerar_relatorio.py` | média | *"índice de concordância de 0,79 com a China"*, com a definição em uma linha |
| 19 | **"Não foi post no Truth Social"** é mais forte que o dado: o arquivo lido tem os 19 posts listados de 25/out até 22h31 da costa leste, e o texto da EFE não diz o canal | `RELATORIO.md` §2; `docs/F1_REACOES.md` §1 | baixa | *"Não foi achado post: 0 dos 19 posts de 25/out listados no arquivo falam do Brasil"* |
| 20 | **"A alegação de fraude de Trump virou restrição de visto"** afirma causa; a §11 pede *"consistente com"* | `RELATORIO.md` §6; `docs/LEITURA_DA_IA.md` | média | *"foi seguida, em X dias, de restrição de visto"* |
| 21 | **"Ele falou em fraude sem prova" (Honduras 2025) e "já usou a comparação com 2020"** não têm fonte no projeto, e a segunda é leitura: a fala cita Biden, não 2020 | `RELATORIO.md` §1 (S7) | baixa | Citar a fonte de Honduras ou tirar *"sem prova"*; trocar por *"citou o nome do Biden"* |
| 22 | **"O presidente pôs o resultado em dúvida"** (S6) sem a atribuição; a fala tem uma fonte só | `RELATORIO.md` §1 (S6) | baixa | *"segundo a EFE"*, como já está na S5 |
| 23 | **Resumo: "20 a 25 eleições"** é texto fixo no gerador; foram 25 levantadas e 19 na conta | `ferramentas/gerar_relatorio.py`; `RESUMO_SIMPLES.md` | baixa | Ler os números do `RESUMO.json` |
| 24 | **Resumo: "Se uma fraude não deixar prova, o mundo reage como se o resultado fosse legítimo"** é a premissa do pré-registro dita como fato | `RESUMO_SIMPLES.md` | baixa | *"O projeto supõe que governo de fora reage ao que dá para mostrar"* |
| 25 | **"A Rússia vendeu 26% do adubo"** é em valor (US$), não em volume | `RELATORIO.md` §5 | baixa | *"26% do valor"* |
| 26 | **A linha "o histórico" da S11 aponta para a taxa da Rússia parabenizar**, que não tem relação com citar interferência | `docs/LEITURA_DA_IA.md` S11; `dados/sintese_suposicoes.csv` | baixa | Trocar por *"sem taxa-base nas fichas"* |
| 27 | **A S12 não resolve no prazo.** Os votos da ONU no conjunto do Voeten vão até 2024 (2025, o ano base, ainda não existe), e o Comtrade de 2027 só sai em 2028 | `docs/PRE_REGISTRO.md` §8; `RELATORIO.md` §1 | média | Emenda: a resolução da S12 sai quando os dois dados de 2027 existirem, com o ano base 2025 dito como pendente |
| 28 | **`conferir_linguagem.py` deixa passar a afirmação que ele deveria pegar.** A janela de *"que "* nos 45 caracteres anteriores libera a frase: *"A análise mostra que não houve fraude"* e *"O dado comprova que houve fraude"* passam. *0 achados* não garante a §11 | `ferramentas/conferir_linguagem.py` (`hipotetico`) | média | Trocar a lista de marcas por contextos explícitos (*"se houve"*, *"dizem que"*, *"lente F"*) e testar com frases que devem falhar |
| 29 | **As 46 fontes da F4 não têm captura com hash**, contra a §9 (*"toda captura com endereço, hora e sha256"*) | `dados/f4_estado_26out.md` | média | Passar as fontes da F4 pelo `capturar.py` |
| 30 | **A ordem da emenda 2 não é verificável.** A emenda tem commit às 10h10min55 e diz ser anterior às fichas; as 50 fichas entram no commit das 10h19. Nada no repositório mostra quando cada passada começou e terminou | `docs/PRE_REGISTRO.md` §13; histórico do git | baixa | Publicar a hora de início e fim de cada passada e as instruções dadas a cada codificador |
| 31 | **A independência das duas passadas não está documentada.** As duas são da IA; não há registro de modelo, instrução ou isolamento, e codificadores com o mesmo modelo tendem a concordar mais (o kappa de 0,92 pode estar inflado) | `docs/F2_FICHA.md`; `dados/casos/` | média | Publicar as instruções de cada passada e dizer quem ou o que codificou cada uma |
| 32 | **A validação "99 de 99" cobre pouco.** 96 itens são fatias de comércio e concordância da ONU (a mesma conta, ano a ano); só 3 taxas-base; nada do teste do passado, do kappa, dos adubos, das terras raras, do saldo ou das contagens da F1 | `ferramentas/validacao_independente.py`; `RELATORIO.md` §7 | média | Incluir o Brier (as três referências), o kappa e os números da seção 2 abaixo; dizer no relatório o que foi e o que não foi validado |
| 33 | **O README ainda cita `apuracao-segundo-turno-2026`**, renomeado pela emenda 3 | `README.md` | baixa | Trocar por `investigacao-segundo-turno-2026` |

Travessão: nenhum nos textos públicos (conferido por busca do caractere). *"Fraude"* afirmada ou negada fora de hipótese: não achei nos textos lidos; os riscos estão nas frases dos achados 19 a 24. Julgamento de intenção: não achei; *"questionamento retórico"* descreve a fala, não a intenção.

---

## 2. Os 10 números refeitos

Refeitos a partir das passadas brutas, dos arquivos do Comtrade e do Voeten e do texto do USGS, sem usar `analise.py` nem `validacao_independente.py`.

| # | Número no `RELATORIO.md` | Refeito | Resultado |
|---|---|---|---|
| 1 | Diferença de 4.430.191 votos e Lula com 51,79% dos válidos | 64.256.232 menos 59.826.041 = 4.430.191; 64.256.232 ÷ 124.082.273 = 51,785% | bate |
| 2 | 19 casos na conta, 6 fora (Costa do Marfim 2010, Geórgia 2003, Honduras 2017, Sérvia 2000, Ucrânia 2004, Venezuela 2013) | os mesmos 6 têm `fecha_com_duas_fontes` falso em ao menos uma passada | bate |
| 3 | EUA parabenizaram em até 30 dias: 7 de 8 na lente L, 0 de 5 na lente F | 7 de 8 e 0 de 5 | bate |
| 4 | Eleição anulada ou refeita: 3 de 6 na lente F, 0 de 10 na lente L | 3 de 6 e 0 de 10 (as 3 são `disputado`, achado 3) | bate |
| 5 | Sanção dos EUA em 12 meses com vencedor adversário: 4 de 5 | 4 de 5 (próximo 1 de 5, neutro 0 de 6) | bate |
| 6 | Concordância média de 95% e kappa mediano de 0,93 | concordância 95,3%; mediana dos 16 kappas 0,9195 | concordância bate; **kappa não bate** (0,92) |
| 7 | Brier 0,191 em 145 previsões; Brasil 2022 0,117, Honduras 2025 0,222, Hungria 2026 0,189 | 0,1913 em 145; 0,1170, 0,2221, 0,1892 | bate |
| 8 | Exportações de 2025: China 28,7%, EUA 10,9%, Rússia 0,4%; importações: 25,8%, 16,3%, 3,5% | 28,69%, 10,93%, 0,44%; 25,82%, 16,26%, 3,50% | bate |
| 9 | Saldo de 2025: déficit de US$ 9,7 bi com os EUA, superávit de US$ 24,1 bi com a China | 38,104 menos 47,786 = menos 9,68; 100,021 menos 75,872 = 24,15 | bate |
| 10 | ONU, 2024: 80% com a China, 63% com a Rússia, 37% com os EUA | `agree` 0,7946, 0,6327, 0,3661 (Brasil é o código 140) | bate (a leitura como *"votou igual"* é o achado 18) |

**Refeitos a mais:** adubos, Rússia com 26,08% do valor importado em 2025 (bate); terras raras, Brasil em 2º com 11 milhões de toneladas, China 44 milhões, EUA 1,9 milhão (bate, e depende de ler a linha da Austrália, *"136,300,000"*, como nota de rodapé 13 mais 6.300.000; lida de outro jeito, o Brasil cai para 3º); C1 pelo número de imprensa, 35.521 ÷ 4.430.191 = 0,80% (bate); citações da F1, 33 de 33 achadas no texto capturado, e os 49 textos capturados batem com o sha256 do manifesto (bate); posts do Truth Social, 0 de 19 em 25/out (bate); captura da F1, *"49 de 42"* (**não bate**: 39 de 42, achado 16).

---

## 3. O teste do passado

**Vaza o caso testado?** Não. Em `teste_do_passado`, a lista `outros` tira o próprio caso antes de calcular a taxa, e a condição (a relação do vencedor com a potência) é uma característica que existia antes da eleição. Dois cuidados, sem vazamento propriamente dito:

- **Casos posteriores entram na taxa** (achado 12). Refeito só com casos de ano anterior ao testado: Brier **0,214** (Brasil 2022 0,101; Honduras 2025 0,237; Hungria 2026 0,189).
- **A relação do vencedor foi codificada hoje, por quem sabe o que aconteceu.** Num caso como Bolívia 2019, *"adversário"* pode ter sido lido com o olho no desfecho. O risco é pequeno, mas existe e não está dito.

**A comparação com 50% é justa?** É correta, mas fraca (achado 13). A referência mais dura pedida, a **taxa geral dos outros casos, sem condicionar na relação do vencedor** (mesmo deixa-um-de-fora, mesma suavização), dá:

| Referência | Brier, 145 previsões | Brasil 2022 | Honduras 2025 | Hungria 2026 | Só os 72 desfechos condicionados |
|---|---|---|---|---|---|
| Chute de 50% | 0,250 | 0,250 | 0,250 | 0,250 | 0,250 |
| Taxa geral dos outros (sem condicionar) | **0,224** | 0,155 | 0,247 | 0,181 | **0,241** |
| Taxa condicionada na relação do vencedor (o do projeto) | 0,191 | 0,117 | 0,222 | 0,189 | **0,174** |
| Condicionada, só com casos anteriores | 0,214 | 0,101 | 0,237 | 0,189 | não calculado |

**O condicionamento ajuda.** O ganho todo está nos 72 desfechos que de fato são condicionados (parabéns dos EUA, da China e da Rússia, não reconhecimento e sanção dos EUA): de 0,241 para 0,174. Nos outros 73 as duas referências são iguais por construção. Na Hungria 2026 o condicionamento piora um pouco (0,181 para 0,189). Com 19 casos e previsões que saem do mesmo campo, a diferença é indicativa, não medida com precisão.

---

## 4. O que falta para um terceiro refazer

1. **Os brutos não estão no repositório.** `dados/brutos/` está no `.gitignore`: os JSON do Comtrade, o `AgreementScores.csv` do Voeten e o PDF do USGS só existem com o hash. A API de prévia do Comtrade é revisada com o tempo, então baixar de novo pode não bater com o sha256. Publicar esses três como anexo de versão (*release*), ou registrar a versão exata do conjunto (Dataverse) e a data.
2. **`requirements.txt` incompleto:** faltam `pandas` (validação) e `matplotlib` (gráficos); nenhuma versão fixada; sem versão do Python; o `capturar.py --navegador` pede `playwright install`.
3. **Os passos de captura refazem páginas vivas.** Rodar `capturar.py` hoje gera outro texto e outro hash. Falta um modo que só confere as capturas guardadas contra o manifesto (o teste já faz isso; dizer no §8 do relatório que é ele que se roda).
4. **As fichas da F2 não têm captura das fontes.** Cada caso traz só URLs; quem refaz relê a internet de hoje. E faltam as instruções de cada passada e o registro de quem as fez (achados 30 e 31).
5. **Quatro tabelas são julgamento escrito à mão** (`sintese_suposicoes.csv`, `hipoteses_veredito.csv`, `criterios_c1_c5.csv`, `quadro_reacoes.csv`). Está certo que sejam, mas o relatório não diz que são, nem de que fonte vem cada célula.
6. **`docs/REVISAO_ADVERSARIAL.md` não existe** e as variantes das objeções não foram calculadas (achado 11).
7. **C1 e C2 dependem de outro projeto sem contrato escrito:** qual arquivo, de qual commit, com qual hash entra aqui.
8. **As emendas que estes achados pedem** (agrupamento da lente F, fonte do comércio, NELDA, coluna da nota de Brier, Laplace, resolução da S12), cada uma dizendo se veio antes ou depois de ver o dado.
