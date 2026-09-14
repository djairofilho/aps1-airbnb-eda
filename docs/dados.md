# Dados e pergunta de pesquisa

## Fonte

Foi utilizado o arquivo **AB_NYC_2019.csv** do dataset
[New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).
A base contém **48.895 anúncios e 16 variáveis**.

O arquivo representa um snapshot da plataforma em 2019, não uma série temporal
de preços. A versão analisada é identificada pelo SHA-256:

```text
e420db40ff10fcb40efc1b5b1648ee0b18a48f4e4537155cecc59fe95d18783a
```

## Pergunta central

> Como localização, tipo de acomodação, disponibilidade e atividade de
> avaliações se relacionam com o preço anunciado de uma diária do Airbnb em
> Nova York em 2019, e como preparar esses dados para um futuro modelo de
> regressão?

## Dicionário das variáveis

| Variável | Tipo | Significado |
|---|---|---|
| `id` | Identificador | Identificador único do anúncio |
| `name` | Texto | Título do anúncio |
| `host_id` | Identificador | Identificador do anfitrião |
| `host_name` | Texto | Nome do anfitrião |
| `neighbourhood_group` | Categórica | Borough de Nova York |
| `neighbourhood` | Categórica | Bairro do anúncio |
| `latitude` | Numérica | Latitude do anúncio |
| `longitude` | Numérica | Longitude do anúncio |
| `room_type` | Categórica | Tipo de acomodação |
| `price` | Numérica | Preço anunciado por noite em dólares |
| `minimum_nights` | Numérica discreta | Mínimo de noites exigido |
| `number_of_reviews` | Numérica discreta | Total de avaliações |
| `last_review` | Data | Data da avaliação mais recente |
| `reviews_per_month` | Numérica | Média mensal na vida do anúncio |
| `calculated_host_listings_count` | Discreta | Anúncios do host na região |
| `availability_365` | Discreta | Dias disponíveis no calendário futuro |

IDs são números no arquivo, mas não representam grandezas. Por isso, não entram
como variáveis quantitativas na análise ou no modelo.

`availability_365` não distingue uma data reservada de uma data bloqueada pelo
anfitrião e, por isso, não mede ocupação. `reviews_per_month` também não significa
avaliações apenas no último mês: é uma média calculada durante a vida do anúncio.
Essas definições seguem o [dicionário][data-dictionary] e as
[premissas metodológicas][data-assumptions] do Inside Airbnb.

[data-dictionary]: https://docs.google.com/spreadsheets/d/1iWCNJcSutYqpULSQHlNyGInUvHg2BoUGoNRIGa6Szc4/edit?usp=sharing
[data-assumptions]: https://insideairbnb.com/data-assumptions/
