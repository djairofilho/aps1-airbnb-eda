# Projeto de Machine Learning — Airbnb em Nova York

[Documentação pública](https://djairofilho.github.io/aps1-airbnb-eda/) ·
[APS1: EDA](notebooks/APS1_Airbnb_EDA.ipynb) ·
[APS2: regressão](notebooks/APS2_Airbnb_Regressao.ipynb) ·
[Dataset](data/raw/AB_NYC_2019.csv)

Exploração e modelagem do conjunto **New York City Airbnb Open Data** para a
disciplina de Machine Learning do Insper.

O projeto investiga como localização, tipo de acomodação, disponibilidade e
atividade de avaliações se relacionam com o preço anunciado por noite no recorte
de Nova York em 2019. A APS1 audita os dados e define o pré-processamento; a
APS2 compara modelos de regressão, avalia o vencedor no teste e o interpreta.

## Autor

Djairo Dantas da Silva Filho

## Conteúdo

- [APS1 — notebook executado](notebooks/APS1_Airbnb_EDA.ipynb)
- [APS2 — notebook executado](notebooks/APS2_Airbnb_Regressao.ipynb)
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

SHA-256 da versão analisada:

```text
e420db40ff10fcb40efc1b5b1648ee0b18a48f4e4537155cecc59fe95d18783a
```

## Como executar com uv

O ambiente principal é gerenciado pelo
[`uv`](https://docs.astral.sh/uv/getting-started/installation/). Para instalar
o Python 3.12, sincronizar as versões registradas no lockfile e abrir o Jupyter
Lab:

```powershell
uv sync --locked
uv run jupyter lab
```

Para executar os dois notebooks sem abrir a interface:

```powershell
uv run jupyter nbconvert --execute --to notebook --inplace notebooks/APS1_Airbnb_EDA.ipynb
uv run jupyter nbconvert --execute --to notebook --inplace notebooks/APS2_Airbnb_Regressao.ipynb --ExecutePreprocessor.timeout=1800
```

## Alternativa com pip

O `requirements.txt` é exportado do ambiente do `uv` para facilitar a execução
em ambientes que utilizam apenas `pip`:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/APS1_Airbnb_EDA.ipynb
python -m jupyter nbconvert --execute --to notebook --inplace notebooks/APS2_Airbnb_Regressao.ipynb --ExecutePreprocessor.timeout=1800
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

### APS1

- O preço anunciado apresenta forte assimetria à direita.
- Acomodações inteiras e anúncios em Manhattan têm preços típicos maiores.
- As ausências em variáveis de avaliação são estruturais para anúncios sem
  avaliações.
- O pipeline separa variáveis numéricas e categóricas e evita ajuste com os
  dados de teste.
- Os dois primeiros componentes do PCA explicam aproximadamente 43,8% da
  variância das features numéricas padronizadas.

### APS2

- Compara Dummy, Ridge e Random Forest por MAE nos mesmos folds do treino.
- Testa uma mudança isolada no encoder: agrupar categorias com menos de 20 anúncios.
- A floresta com categorias raras agrupadas obteve MAE de **US$ 65,04** na
  validação e **US$ 63,08** no teste reservado; a melhora de **US$ 0,09** na
  validação após agrupar categorias é pequena.
- Usa SHAP para explicar resultados globais e três previsões individuais.

Os valores observados, os gráficos e a discussão completa estão no [notebook da APS2](notebooks/APS2_Airbnb_Regressao.ipynb) e na [documentação pública](https://djairofilho.github.io/aps1-airbnb-eda/aps2/).

## Limitações

Os dados formam um snapshot de anúncios disponíveis em 2019, não uma série
histórica de preços nem um registro de reservas concluídas. Portanto, preço
anunciado não equivale a preço pago, ocupação, demanda ou receita. As associações
encontradas não demonstram causalidade nem descrevem o mercado atual.
