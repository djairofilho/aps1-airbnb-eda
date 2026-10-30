# Reprodução

## Requisitos

- Git;
- uv;
- acesso à internet apenas se for necessário baixar dependências ou o dataset.

O repositório fixa Python 3.12 e registra as versões resolvidas em `uv.lock`.

## Instalação

```powershell
git clone https://github.com/djairofilho/aps-airbnb-eda.git
cd aps-airbnb-eda
uv sync --locked
```

## Executar os notebooks

A APS1 documenta a exploração; a APS2 reproduz as etapas necessárias de preparação e executa a modelagem. Cada notebook pode ser iniciado com um kernel limpo.

```powershell
uv run jupyter nbconvert --execute --to notebook --inplace `
  notebooks/APS1_Airbnb_EDA.ipynb
uv run jupyter nbconvert --execute --to notebook --inplace `
  notebooks/APS2_Airbnb_Regressao.ipynb `
  --ExecutePreprocessor.timeout=1800
```

Ou abrir o ambiente interativo:

```powershell
uv run jupyter lab
```

## Construir a documentação

```powershell
uv run python scripts/export_docs.py
uv run python scripts/export_aps2_docs.py
uv run mkdocs build --strict
```

Para visualizar localmente:

```powershell
uv run mkdocs serve
```

## Compatibilidade com pip

O `requirements.txt` é gerado a partir do ambiente bloqueado:

```powershell
uv export --all-groups `
  --no-emit-project `
  --no-hashes `
  --format requirements.txt `
  --output-file requirements.txt
```

Depois pode ser instalado com:

```powershell
python -m pip install -r requirements.txt
```

O CSV local é verificado por SHA-256. Na ausência dele, os notebooks podem obtê-lo da fonte indicada via `kagglehub`; a execução exige o mesmo conteúdo validado pelo hash.
