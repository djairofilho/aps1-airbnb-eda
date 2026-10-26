# Projeto de Machine Learning — Airbnb NYC

**Autor:** Djairo Dantas da Silva Filho · **Disciplina:** Machine Learning, Insper · **Dados:** anúncios de Nova York em 2019

O projeto investiga o **preço anunciado por noite** de imóveis no Airbnb em duas etapas. Cada linha do dataset representa um anúncio, e o preço não equivale ao valor pago pelo hóspede. A primeira etapa estuda os dados e define o pré-processamento; a segunda compara modelos de regressão e avalia o escolhido em dados reservados.

| Etapa | Data | Pergunta principal | Entregas |
|---|---|---|---|
| **APS1 — exploração dos dados** | 14/09/2026 | Como as variáveis se distribuem e se relacionam com o preço? | Auditoria de qualidade, gráficos, decisões de pré-processamento e PCA. |
| **APS2 — modelagem e avaliação** | 26/10/2026 | Quão bem conseguimos prever o preço anunciado de um anúncio não usado no ajuste? | Três modelos, validação cruzada, mudança no pipeline, avaliação no teste, SHAP e discussão crítica. |

[Explorar a APS1](aps1.md){ .md-button }
[Ver a APS2](aps2/index.md){ .md-button .md-button--primary }

## Como as etapas se conectam

```text
CSV de 2019
    → APS1: limpeza determinística, divisão treino/teste e EDA no treino
    → APS1: pipeline de imputação, padronização e one-hot
    → APS2: modelos e seleção somente no treino
    → APS2: avaliação final no teste reservado
```

A APS2 reproduz a divisão e o pipeline definidos na APS1. A documentação de cada etapa permanece separada no menu, com seus próprios resultados, notebook e limitações. Veja [como reproduzir o projeto](reproducao.md).
