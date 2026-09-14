# Limitações

## O que os dados permitem afirmar

Os resultados descrevem associações entre características dos anúncios e seus
preços anunciados em Nova York em 2019.

## O que os dados não permitem afirmar

- preço efetivamente pago;
- ocupação, receita ou demanda real;
- efeito causal de região ou tipo de acomodação;
- comportamento do mercado atual;
- qualidade do imóvel ou experiência do hóspede;
- desempenho uniforme em boroughs pouco representados.

## Riscos para modelagem

- cauda longa do target;
- alta cardinalidade de bairro;
- extremos potencialmente influentes;
- variáveis omitidas;
- concentração geográfica;
- possível diferença de erro entre grupos.

## Próximos controles na APS2

1. Comparar target original e transformação log1p.
2. Usar validação cruzada somente no treino.
3. Reportar MAE e RMSE na escala de dólares.
4. Analisar resíduos e erros por borough e tipo.
5. Comparar baseline linear com modelos não lineares.
6. Avaliar se categorias raras de bairro precisam de agrupamento.
