# Plano da APS1 — EDA do Airbnb em Nova York

## 1. Definição do projeto

### Dataset

**New York City Airbnb Open Data**, publicado no Kaggle, com um snapshot de
anúncios do Airbnb em Nova York em 2019.

Arquivo esperado: `AB_NYC_2019.csv`.

### Tipo de problema

**Regressão**.

### Target

`price`: preço anunciado por noite, em dólares.

### Pergunta central

> Como localização, tipo de acomodação, disponibilidade e atividade de avaliações
> se relacionam com o preço anunciado de uma diária do Airbnb em Nova York em
> 2019, e como preparar esses dados para um futuro modelo de regressão?

Essa formulação é cuidadosa: o dataset contém anúncios, não reservas efetivamente
realizadas. Portanto, o projeto analisa **preços anunciados**, e não receita,
ocupação real ou demanda comprovada.

## 2. Aplicação da rubrica ao projeto de regressão

Neste projeto, `price` é um target numérico contínuo. Portanto, os requisitos
gerais da rubrica são aplicados com diagnósticos adequados à regressão:

| Requisito | Aplicação no Airbnb |
|---|---|
| Distribuição do target | Analisar assimetria, concentração e extremos. |
| Categóricas e target | Comparar a distribuição de `price` entre grupos. |
| PCA | Avaliar a estrutura numérica e padrões entre grupos. |

O target permanece contínuo durante toda a análise e na modelagem prevista para
a APS2.

## 3. Dicionário das variáveis

Validar os nomes e tipos depois do carregamento do CSV.

| Variável | Tipo esperado | Significado | Uso futuro |
|---|---|---|---|
| `id` | ID | Anúncio | Remover |
| `name` | Texto | Título | Excluir ou derivar texto |
| `host_id` | ID | Anfitrião | Não tratar como contínua |
| `host_name` | Texto | Nome do anfitrião | Remover |
| `neighbourhood_group` | Categórica | Borough | Manter |
| `neighbourhood` | Categórica | Bairro | Controlar cardinalidade |
| `latitude` | Geográfica | Latitude | Manter |
| `longitude` | Geográfica | Longitude | Manter |
| `room_type` | Categórica | Tipo de acomodação | Manter |
| `price` | Numérica | Preço anunciado | Target |
| `minimum_nights` | Discreta | Mínimo de noites | Investigar extremos |
| `number_of_reviews` | Discreta | Total de avaliações | Manter |
| `last_review` | Data | Última avaliação | Transformar ou excluir |
| `reviews_per_month` | Numérica | Média histórica | Imputar com contexto |
| `calculated_host_listings_count` | Discreta | Anúncios na região | Manter |
| `availability_365` | Discreta | Dias disponíveis | Não é ocupação |

## 4. Estrutura recomendada do notebook

### 0. Capa

Incluir:

- título do projeto;
- nomes dos integrantes;
- disciplina e turma;
- data de entrega;
- link e referência do dataset;
- pergunta central.

### 1. Configuração

Importar obrigatoriamente:

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.compose import ColumnTransformer
from sklearn.decomposition import PCA
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
```

Definir:

```python
RANDOM_STATE = 42
TEST_SIZE = 0.20
```

Configurar um tema visual consistente e não esconder warnings globalmente.

### 2. Carregamento e inspeção inicial

Exibir e interpretar:

- `head()`;
- `shape`;
- `info()`;
- quantidade de valores únicos;
- amostra de valores de cada variável categórica;
- intervalo de datas em `last_review`.

Converter `last_review` com `pd.to_datetime(..., errors="coerce")`.

Não imprimir milhares de linhas nem grandes tabelas sem necessidade.

### 3. Auditoria de qualidade

Investigar:

- ausentes em quantidade e percentual;
- duplicatas completas;
- duplicidade de `id`;
- preços iguais ou menores que zero;
- coordenadas fora dos limites plausíveis de Nova York;
- `availability_365` fora do intervalo de 0 a 365;
- `minimum_nights` extremamente alto;
- valores incompatíveis entre `number_of_reviews`, `reviews_per_month` e
  `last_review`;
- espaços e grafias diferentes nas categorias.

#### Ausências esperadas

É provável que existam ausentes em `name`, `host_name`, `last_review` e
`reviews_per_month`. A causa da ausência importa:

- se `number_of_reviews == 0`, a ausência de `last_review` é estrutural;
- no mesmo caso, `reviews_per_month` pode ser preenchido com zero;
- se há avaliações, mas `reviews_per_month` está ausente, existe uma
  inconsistência que precisa ser quantificada.

Não preencher tudo automaticamente com média ou moda antes dessa verificação.

### 4. Limpeza mínima anterior ao split

Antes da divisão, fazer apenas operações que não aprendem estatísticas das
features:

- remover duplicatas somente se forem confirmadas como registros repetidos;
- remover registros sem target;
- tratar `price <= 0` como target inválido, após mostrar quantos casos existem;
- corrigir tipos e representações evidentemente incorretas;
- separar `X` e `y`.

Valores altos de `price` não devem ser removidos apenas por serem outliers. Eles
podem representar acomodações reais de luxo.

### 5. Divisão entre treino e teste

Usar:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
)
```

Não usar `stratify=y`, pois o target é contínuo. Se o grupo decidir estratificar
por faixas de preço, terá de justificar a criação e a estabilidade dessas faixas;
isso não é necessário para a APS1.

Depois da inspeção estrutural e da limpeza determinística, tomar decisões e
ajustar imputadores, scalers, encoders e PCA somente com o treino. Manter o teste
reservado para a APS2.

## 5. Análise univariada

O enunciado limita as visualizações. Cada figura pode ter subplots relacionados,
mas não é recomendável tentar contornar artificialmente o limite.

### Estatísticas numéricas

Produzir uma tabela para **todas** as variáveis numéricas com:

- média;
- mediana;
- desvio padrão;
- mínimo;
- primeiro e terceiro quartis;
- máximo;
- percentual de zeros, quando relevante.

Não interpretar `id` e `host_id` como medidas quantitativas, mesmo que o Pandas
os identifique como números.

### Três figuras numéricas sugeridas

1. Histograma de `price` em escala original e/ou `log1p`.
2. Boxplot de `minimum_nights`.
3. Histograma de `availability_365`.

Na visualização de `price`, é aceitável limitar o eixo ou exibir um segundo
subplot sem os valores mais extremos, desde que:

- o corte seja informado no título ou na legenda;
- nenhuma observação seja silenciosamente removida da análise;
- as estatísticas completas continuem disponíveis.

### Três figuras categóricas sugeridas

1. Contagem de anúncios por `neighbourhood_group`.
2. Contagem por `room_type`.
3. Contagem dos bairros mais frequentes em `neighbourhood`.

Para `neighbourhood`, mostrar apenas as categorias mais frequentes e informar
quantas categorias existem no total.

## 6. Análise bivariada e multivariada

### Relações entre variáveis numéricas: até três figuras

1. Matriz de correlação das variáveis numéricas úteis, incluindo `price`.
2. Scatter plot de `minimum_nights` versus `price`.
3. Scatter plot de `availability_365` versus `price`.

Usar transparência, amostragem reprodutível ou escala logarítmica quando houver
sobreposição. A amostra deve servir apenas para visualização, não para alterar o
dataset usado no pipeline.

Correlação linear baixa não significa ausência de relação. Os padrões podem ser
assimétricos, segmentados por região ou não lineares.

### Variáveis categóricas versus target: até três figuras

1. Distribuição de `price` por `room_type`.
2. Distribuição de `price` por `neighbourhood_group`.
3. Mediana de `price` nos bairros com quantidade mínima de anúncios definida e
   justificada.

Preferir mediana ou boxplot a uma barra baseada apenas na média, pois `price`
tende a possuir cauda longa.

### Variáveis numéricas versus categóricas: até três figuras

1. `minimum_nights` por `room_type`.
2. `availability_365` por `neighbourhood_group`.
3. `reviews_per_month` por `room_type`.

### Regra para interpretar cada figura

Escrever logo abaixo:

1. o padrão observado;
2. por que ele é relevante;
3. qual decisão ou hipótese ele sugere;
4. por que não permite afirmar causalidade.

## 7. Outliers e distribuição do target

Separar três ideias que frequentemente são confundidas:

1. **Valor inválido:** por exemplo, preço zero para uma diária paga.
2. **Valor improvável:** pode ser erro, mas exige investigação.
3. **Valor extremo plausível:** pode ser uma acomodação legítima de luxo.

Estratégia recomendada:

- remover somente targets claramente inválidos, com contagem e justificativa;
- manter extremos plausíveis na base original;
- usar eixos limitados apenas para tornar gráficos legíveis;
- considerar `log1p(price)` na APS2, usando transformação reversível do target;
- comparar métricas na escala original na APS2.

Para `minimum_nights`, investigar valores extremos e sua plausibilidade. Não
remover automaticamente tudo o que estiver além de 1,5 IQR.

## 8. Feature engineering justificável

Manter a APS1 simples e reproduzível. Boas transformações candidatas:

### Data da última avaliação

Em vez de usar a data bruta, criar `days_since_last_review` usando como referência
a data máxima observada no próprio período do dataset, e não a data atual.

Também criar um indicador como `has_reviews` ou `has_last_review`.

### Títulos dos anúncios

Para um baseline, excluir `name`. Como extensão, podem ser criadas features
simples, como comprimento do título, sem tentar NLP nesta etapa.

### Identificadores

- excluir `id` do modelo;
- não tratar `host_id` como número contínuo;
- usar `calculated_host_listings_count` para representar a escala do anfitrião.

### Localização

Manter `latitude`, `longitude`, `neighbourhood_group` e `neighbourhood`. Elas
representam granularidades diferentes, mas é necessário comentar a possível
redundância.

## 9. Decisões iniciais de pré-processamento

| Grupo | Estratégia inicial | Justificativa |
|---|---|---|
| Numéricas | Mediana + `StandardScaler` | Escalas comparáveis para PCA |
| Avaliações/mês | Zero sem reviews | Ausência pode ser estrutural |
| Categóricas | Moda ou `Missing` | Evita perda de linhas |
| Nominais | `OneHotEncoder` | Não introduz ordem artificial |
| `neighbourhood` | Agrupar raras, se preciso | Controla cardinalidade |
| Texto e IDs | Remover do baseline | Sem sentido numérico direto |
| Assimétricas | Avaliar `log1p` | Reduz o efeito da cauda |

A implementação deve manter três cuidados adicionais:

- preencher `reviews_per_month` com zero somente quando
  `number_of_reviews == 0`;
- usar `OneHotEncoder(handle_unknown="ignore")` nas categóricas nominais;
- agrupar categorias raras de `neighbourhood` apenas se a EDA justificar.

A escolha final entre moda e categoria `Missing` deve nascer da auditoria de
ausentes. Não apresentar essa tabela como decisão comprovada antes de executar a
EDA.

## 10. PCA

O PCA deve ser usado para visualização das features numéricas, não como prova de
que o preço pode ser bem previsto.

### Features candidatas

- `latitude`;
- `longitude`;
- `minimum_nights`;
- `number_of_reviews`;
- `reviews_per_month`;
- `calculated_host_listings_count`;
- `availability_365`.

Excluir `id`, `host_id` e `price` do ajuste do PCA.

### Procedimento

1. Imputar as features numéricas usando somente `X_train`.
2. Padronizar usando `StandardScaler`.
3. Ajustar `PCA(n_components=2)` no treino.
4. Mostrar a variância explicada por PC1 e PC2.
5. Inspecionar os loadings.
6. Fazer PC1 versus PC2 com cor por `room_type` ou `neighbourhood_group`.
7. Como complemento, usar `price` ou suas faixas apenas como recurso visual.

Registrar que `StandardScaler` e PCA continuam sensíveis a extremos, mesmo após
a padronização.

Conclusões válidas incluem a ausência de grupos claros. PCA procura direções de
maior variância e não maximiza a capacidade de prever `price`.

## 11. Pipeline de pré-processamento

### Features sugeridas para o baseline da APS2

```python
numeric_features = [
    "latitude",
    "longitude",
    "minimum_nights",
    "number_of_reviews",
    "reviews_per_month",
    "calculated_host_listings_count",
    "availability_365",
]

categorical_features = [
    "neighbourhood_group",
    "neighbourhood",
    "room_type",
]
```

### Estrutura

```python
numeric_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler()),
    ]
)

categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("encoder", OneHotEncoder(handle_unknown="ignore")),
    ]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("numeric", numeric_pipeline, numeric_features),
        ("categorical", categorical_pipeline, categorical_features),
    ]
)

preprocessing_pipeline = Pipeline(
    steps=[("preprocessor", preprocessor)]
)
```

Esse é um ponto de partida. Se a EDA justificar transformações customizadas,
elas devem ser incorporadas ao pipeline, e não executadas manualmente em treino
e teste de maneiras diferentes.

### Verificações obrigatórias

- `fit_transform(X_train)` executa sem erros;
- `transform(X_test)` executa sem novo `fit`;
- treino e teste transformados têm a mesma quantidade de colunas;
- categorias presentes apenas no teste não causam erro;
- o número de features antes e depois do one-hot é registrado;
- nenhuma estatística do teste influencia o treinamento.

## 12. Síntese final esperada

Terminar o notebook respondendo:

- como os preços estão distribuídos;
- quais regiões e tipos de acomodação apresentam maiores diferenças de preço;
- quais problemas de qualidade foram encontrados;
- como os ausentes serão tratados e por quê;
- quais valores extremos foram mantidos, removidos ou apenas limitados nos
  gráficos;
- o que o PCA revelou;
- quais features entrarão no pipeline;
- quais são as limitações do estudo.

Limitações importantes:

- os dados representam um recorte de 2019;
- preço anunciado não é o mesmo que preço efetivamente pago;
- o dataset não mostra ocupação ou receita real;
- associação entre localização e preço não demonstra causalidade;
- conclusões históricas não devem ser apresentadas como retrato atual do mercado.

## 13. Ordem de execução

```text
baixar AB_NYC_2019.csv
    -> criar capa e pergunta central
    -> documentar as 16 colunas
    -> auditar qualidade e target
    -> realizar limpeza determinística
    -> separar treino e teste
    -> fazer EDA no treino
    -> decidir o pré-processamento
    -> construir e validar o pipeline
    -> aplicar e interpretar PCA
    -> escrever síntese e limitações
    -> reiniciar o kernel e executar tudo
```

## 14. Cronograma até 14/09

### 11/09 — dados e qualidade

- baixar o CSV;
- criar o notebook e a capa;
- escrever dicionário das variáveis;
- inspecionar ausentes, duplicatas, tipos e inconsistências;
- analisar `price <= 0` e extremos.

### 12/09 — EDA

- fazer estatísticas numéricas;
- produzir as visualizações selecionadas;
- escrever conclusões logo abaixo de cada figura;
- documentar como cada requisito foi aplicado à regressão.

### 13/09 — pipeline e PCA

- finalizar as decisões de pré-processamento;
- construir e testar o `ColumnTransformer`;
- executar e interpretar o PCA;
- escrever a síntese e as limitações.

### 14/09 — revisão e entrega

- executar o notebook do início ao fim;
- verificar caminhos relativos e dependências;
- revisar títulos, unidades, rótulos e legendas;
- revisar ortografia, identificação e referências;
- verificar permissões do link de entrega;
- enviar com antecedência.

## 15. Divisão sugerida para a dupla

### Pessoa A

- dicionário de dados;
- auditoria de qualidade;
- análise univariada;
- texto sobre ausentes e outliers.

### Pessoa B

- análises bivariada e multivariada;
- PCA;
- `ColumnTransformer` e pipeline;
- revisão contra vazamento de dados.

### Trabalho conjunto

- selecionar as figuras finais;
- decidir quais registros e features manter;
- interpretar os resultados;
- revisar e executar o notebook completo.

## 16. Checklist para conceito A

- [x] O arquivo usado é o `AB_NYC_2019.csv` da fonte definida.
- [x] A capa contém nomes, título, data e referência.
- [x] A pergunta central fala de preço **anunciado** em 2019.
- [x] As 16 variáveis foram explicadas.
- [x] Shape, tipos, ausentes, duplicatas e inconsistências foram investigados.
- [x] Foi explicado que `price` é contínuo e sua distribuição foi investigada.
- [x] A distribuição e os extremos de `price` foram analisados.
- [x] A divisão treino/teste ocorreu antes do ajuste dos transformadores.
- [x] As estatísticas incluem todas as variáveis numéricas relevantes.
- [x] Os limites de gráficos foram respeitados.
- [x] Todos os gráficos têm título, eixos, unidades e interpretação.
- [x] Média e mediana não foram tratadas como equivalentes em distribuições
      assimétricas.
- [x] Ausências em avaliações foram interpretadas pelo contexto.
- [x] IDs não foram tratados como grandezas numéricas no modelo.
- [x] Remoções e transformações foram justificadas com evidências.
- [x] O PCA foi ajustado em numéricas imputadas e padronizadas.
- [x] O pipeline funciona no teste sem novo `fit`.
- [x] O texto não confunde associação com causalidade.
- [x] As limitações temporais e de representatividade foram discutidas.
- [x] O notebook executa do início ao fim sem erros.

## 17. Referências

- [New York City Airbnb Open Data — Kaggle](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data)
- [Fonte e downloads — Inside Airbnb](https://insideairbnb.com/get-the-data/)
- [ColumnTransformer com tipos mistos — scikit-learn](https://scikit-learn.org/stable/auto_examples/compose/plot_column_transformer_mixed_types.html)
- [Documentação de PCA — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html)
- [Documentação de train_test_split — scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html)
