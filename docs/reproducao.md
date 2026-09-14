# Reprodução

## Requisitos

- Git;
- uv;
- acesso à internet apenas se for necessário baixar dependências ou o dataset.

O repositório fixa Python 3.12 e registra as versões resolvidas em uv.lock.

## Instalação

    git clone https://github.com/djairofilho/aps1-airbnb-eda.git
    cd aps1-airbnb-eda
    uv sync --locked

## Executar o notebook

    uv run jupyter nbconvert --execute --to notebook --inplace notebooks/APS1_Airbnb_EDA.ipynb

Ou abrir o ambiente interativo:

    uv run jupyter lab

## Construir a documentação

    uv run python scripts/export_docs.py
    uv run mkdocs build --strict

Para visualizar localmente:

    uv run mkdocs serve

## Compatibilidade com pip

O requirements.txt é gerado a partir do ambiente bloqueado:

    uv export --all-groups --no-emit-project --no-hashes --format requirements.txt --output-file requirements.txt

Depois pode ser instalado com:

    python -m pip install -r requirements.txt
