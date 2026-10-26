# APS1 — exploração dos dados

**Entrega:** 14/09/2026 · **Autor:** Djairo Dantas da Silva Filho

A primeira etapa verifica se os dados permitem estudar o **preço anunciado por noite** e prepara as variáveis para a regressão. O conjunto contém 48.895 anúncios e 16 colunas; após excluir 11 preços não positivos, 48.884 anúncios permanecem. A análise exploratória usa apenas a parte de treino da divisão preservada para a APS2.

## O que cada parte responde

| Página | Pergunta |
|---|---|
| [Dados e pergunta](dados.md) | O que representa cada linha e cada variável? |
| [Qualidade e vieses](qualidade.md) | Quais ausências, extremos e diferenças de representatividade exigem cuidado? |
| [Resultados da EDA](resultados.md) | Como preço, localização, tipo e outras variáveis se distribuem e se relacionam? |
| [Pré-processamento](preprocessamento.md) | Como transformar as variáveis sem usar informação do teste? |
| [PCA](pca.md) | O que a projeção das variáveis numéricas revela e o que não revela? |
| [Limitações](limitacoes.md) | Até onde os dados e a EDA permitem concluir? |

O preço tem uma cauda longa; tipo de acomodação e localização distinguem grupos com preços típicos diferentes. Valores ausentes de avaliação são estruturais para anúncios sem reviews. Essas observações motivaram o pipeline de imputação, padronização e one-hot, que é o ponto de partida da [APS2](aps2/index.md).

[Abrir o notebook da APS1](notebook.md){ .md-button }
[Ir para a APS2](aps2/index.md){ .md-button .md-button--primary }
