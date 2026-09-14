# Checklist da rubrica

| Requisito | Evidência |
|---|---|
| Dataset correto | Arquivo, referência do Kaggle e SHA-256 verificado |
| Identificação, título e data | Capa do notebook e página inicial |
| Pergunta sobre preço anunciado | Objetivo e pergunta central |
| Explicação das 16 variáveis | Dicionário de dados |
| Shape, tipos e ausências | Auditoria de qualidade |
| Inconsistências e duplicatas | Checks explícitos no notebook |
| Natureza do target | `price` contínuo; distribuição e extremos analisados |
| Distribuição e extremos do `target` | Histogramas, quantis e tabelas |
| Split antes dos transformadores | Fluxo documentado e código |
| Estatísticas numéricas | Média, mediana, desvio e zeros |
| Sensibilidade das correlações | Pearson, Spearman e `log1p(price)` comparados |
| Limites de gráficos | Três grupos por relação, com subplots relacionados |
| Títulos, eixos e interpretações | Figuras e textos associados |
| Média versus mediana | Diferença discutida para target assimétrico |
| Ausências de avaliações | Interpretação estrutural validada |
| IDs fora da modelagem | Exclusão explícita e justificada |
| Remoções justificadas | Apenas targets inválidos removidos |
| PCA imputado e padronizado | Pipeline numérico ajustado no treino |
| Pipeline transforma teste | Teste sem novo `fit` e categoria inédita |
| Associação não é causalidade | Limites declarados |
| Limitações e vieses | Página específica de representatividade |
| Execução completa | Notebook salvo sem erros |

## Evidência de documentação aberta

Este site apresenta narrativa, visualizações, metodologia, notebook completo e
instruções de reprodução em uma URL pública. O código-fonte permanece disponível
no repositório associado.
