# APS1 — limitações

Estas limitações dizem respeito ao recorte exploratório. A [discussão crítica da APS2](aps2/interpretacao.md) examina outras limitações do modelo e dos dados.

## O que os dados permitem afirmar

Os resultados descrevem associações entre características e preços anunciados
no snapshot de Nova York em 2019.

## O que os dados não permitem afirmar

- preço efetivamente pago;
- evolução dos preços ao longo de 2019;
- ocupação, receita ou demanda real;
- efeito causal de região ou tipo de acomodação;
- comportamento do mercado atual;
- qualidade do imóvel ou experiência do hóspede;
- desempenho uniforme em boroughs pouco representados.

## Riscos para modelagem

- cauda longa do target;
- alta cardinalidade de bairro;
- extremos potencialmente influentes;
- sensibilidade de Pearson, `StandardScaler` e PCA aos extremos;
- variáveis omitidas;
- concentração geográfica;
- possível diferença de erro entre grupos.

## Questões levadas à APS2

1. Validar os modelos apenas no treino e reservar o teste para a avaliação final.
2. Reportar MAE e RMSE na escala de dólares.
3. Analisar resíduos e erros por borough e tipo.
4. Comparar um modelo linear com um conjunto de árvores e um Dummy.
5. Testar o agrupamento de categorias raras de bairro.

A transformação `log1p` do target continua como hipótese para uma investigação posterior. A APS2 mantém a escala original para comparar de modo isolado a mudança no encoder.
