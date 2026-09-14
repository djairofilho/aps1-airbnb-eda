# APS1 — EDA dos anúncios do Airbnb em Nova York

[Documentação pública](https://djairofilho.github.io/aps1-airbnb-eda/) ·
[Notebook](notebooks/APS1_Airbnb_EDA.ipynb) ·
[Dataset](data/raw/AB_NYC_2019.csv)

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
- [Configuração do projeto](pyproject.toml)
- [Ambiente reproduzível](uv.lock)
- [Dependências compatíveis com `pip`](requirements.txt)

## Fonte dos dados

O notebook utiliza o arquivo `AB_NYC_2019.csv` do dataset
[New York City Airbnb Open Data](https://www.kaggle.com/datasets/dgomonov/new-york-city-airbnb-open-data).

O CSV está disponível em `data/raw/AB_NYC_2019.csv`. Se o arquivo não estiver
presente em outra execução, o notebook também pode usar `kagglehub` para obtê-lo
da fonte indicada.

## Como executar com uv

O ambiente principal é gerenciado pelo
[`uv`](https://docs.astral.sh/uv/getting-started/installation/). Para instalar
o Python 3.12, sincronizar as versões registradas no lockfile e abrir o Jupyter
Lab:

```powershell
uv sync --locked
uv run jupyter lab
```

Para executar o notebook completo sem abrir a interface:

```powershell
uv run jupyter nbconvert --execute --to notebook --inplace notebooks/APS1_Airbnb_EDA.ipynb
```

## Alternativa com pip

O `requirements.txt` é exportado do ambiente do `uv` para facilitar a execução
em ambientes que utilizam apenas `pip`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/APS1_Airbnb_EDA.ipynb
```

Ao alterar dependências, atualize o lockfile e gere novamente o arquivo de
compatibilidade:

```powershell
uv lock
uv export --all-groups `
  --no-emit-project `
  --no-hashes `
  --format requirements.txt `
  --output-file requirements.txt
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
