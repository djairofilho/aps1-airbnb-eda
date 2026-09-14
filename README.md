# APS1 — EDA dos anúncios do Airbnb em Nova York

Análise exploratória do conjunto **New York City Airbnb Open Data**, realizada
para a disciplina de Machine Learning do Insper.

O projeto investiga como localização, tipo de acomodação, disponibilidade e
atividade de avaliações se relacionam com o preço anunciado de uma diária em
Nova York em 2019. Esta é a primeira etapa de um projeto de regressão.

## Autor

Djairo Dantas da Silva Filho

## Conteúdo

- [Notebook executado](notebooks/APS1_Airbnb_EDA.ipynb)
- [Plano e checklist da APS1](PLANO_APS1_AIRBNB.md)
- [Dependências](requirements.txt)

## Fonte dos dados

O notebook utiliza o arquivo `AB_NYC_2019.csv` do dataset
[New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).

O CSV está disponível em `data/raw/AB_NYC_2019.csv`. Se o arquivo não estiver
presente em outra execução, o notebook também pode usar `kagglehub` para obtê-lo
da fonte indicada.

## Como executar

Crie um ambiente virtual, instale as dependências e execute o notebook:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/APS1_Airbnb_EDA.ipynb
```

Também é possível abrir o notebook no Jupyter Lab:

```powershell
python -m jupyter lab
```

## Principais resultados

- O preço anunciado apresenta forte assimetria à direita.
- Acomodações inteiras e anúncios em Manhattan têm preços típicos maiores.
- As ausências em variáveis de avaliação são estruturais para anúncios sem
  avaliações.
- O pipeline separa variáveis numéricas e categóricas e evita ajuste com os
  dados de teste.
- Os dois primeiros componentes do PCA explicam aproximadamente 43,8% da
  variância das features numéricas padronizadas.

## Limitações

Os dados representam anúncios de 2019, não reservas concluídas. Portanto, preço
anunciado não equivale a preço pago, ocupação, demanda ou receita. As associações
encontradas não demonstram causalidade nem descrevem o mercado atual.
