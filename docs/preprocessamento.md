# APS1 — pré-processamento

Este é o ponto de partida reproduzido no [notebook da APS2](aps2/notebook.md). Na modelagem, uma cópia não ajustada do pré-processador entra em cada fold da validação cruzada.

## Separação sem vazamento

A limpeza anterior ao split contém apenas operações determinísticas: remoção de
duplicatas completas, remoção de targets inválidos e registro da ausência
estrutural de avaliações.

```text
dados após limpeza determinística
    ├── treino (80%) → aprende mediana, escala e categorias
    └── teste  (20%) → recebe as transformações aprendidas
```

Nenhum método `fit` recebe `X_test`.

## Estratégias adotadas

| Grupo | Estratégia | Justificativa |
|---|---|---|
| Numéricas | Imputação pela mediana | Menor sensibilidade à assimetria |
| Numéricas | `StandardScaler` | Escalas comparáveis; sensível a extremos |
| Categóricas | Imputação pela moda | Evita perda de registros |
| Categóricas | One-hot encoding | Não cria ordem artificial |
| Categoria nova | `handle_unknown="ignore"` | Aceita valores novos |
| IDs e nomes | Exclusão | Sem sentido quantitativo ou alta cardinalidade |
| Target extremo | Manutenção | Não há evidência suficiente de erro |
| Target assimétrico | Manter em US$ na APS2 | Permite isolar o efeito da mudança no encoder; `log1p` permanece hipótese futura |

## Features do baseline

Numéricas:

- latitude e longitude;
- mínimo de noites;
- total e média mensal de avaliações;
- quantidade de anúncios do anfitrião;
- disponibilidade anual;
- indicador de existência de avaliações.

Categóricas:

- borough;
- bairro;
- tipo de acomodação.

O pipeline foi testado no conjunto de teste e também com uma categoria
artificial nunca observada no treino, sem novo ajuste.
