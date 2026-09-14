# Dados e pergunta de pesquisa

## Fonte

Foi utilizado o arquivo **AB_NYC_2019.csv** do dataset
[New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).
A base contém **48.895 anúncios e 16 variáveis**.

## Pergunta central

> Como localização, tipo de acomodação, disponibilidade e atividade de
> avaliações se relacionam com o preço anunciado de uma diária do Airbnb em
> Nova York em 2019, e como preparar esses dados para um futuro modelo de
> regressão?

## Dicionário das variáveis

| Variável | Tipo | Significado |
|---|---|---|
| id | Identificador | Identificador único do anúncio |
| name | Texto | Título do anúncio |
| host_id | Identificador | Identificador do anfitrião |
| host_name | Texto | Nome do anfitrião |
| neighbourhood_group | Categórica | Borough de Nova York |
| neighbourhood | Categórica | Bairro do anúncio |
| latitude | Numérica | Latitude do anúncio |
| longitude | Numérica | Longitude do anúncio |
| room_type | Categórica | Tipo de acomodação |
| price | Numérica | Preço anunciado por noite em dólares |
| minimum_nights | Numérica discreta | Mínimo de noites exigido |
| number_of_reviews | Numérica discreta | Total de avaliações |
| last_review | Data | Data da avaliação mais recente |
| reviews_per_month | Numérica | Média de avaliações por mês |
| calculated_host_listings_count | Numérica discreta | Anúncios do anfitrião |
| availability_365 | Numérica discreta | Dias disponíveis em 365 dias |

IDs são números no arquivo, mas não representam grandezas. Por isso, não entram
como variáveis quantitativas na análise ou no modelo.
