# Revisão da APS1 e prevenção de erros na APS2

Revisão de 30/10/2026. A nota **8,5 na APS1** foi informada pelo autor. Não foram disponibilizados comentários do professor nem a versão exata do arquivo submetido. Portanto, os pontos abaixo são **hipóteses de desconto e problemas observados na versão local**, não uma reconstrução comprovada da correção.

A análise confronta os notebooks com o [enunciado oficial](https://colab.research.google.com/drive/1sW6GFmk9OxxCs072sQWSxA7EyugpUBN2), indicado pela [página do projeto](https://insper.github.io/ML/pt/2026.2/project/). A rubrica distingue a simples presença das tarefas da profundidade das análises, das justificativas e da apresentação. Ter um checklist preenchido não comprova o nível máximo.

## Possíveis pontos de desconto na APS1

| Ponto observado | Evidência na versão local | Por que merece atenção | Aplicação na APS2 |
|---|---|---|---|
| Interpretações genéricas | Na seção 7, a leitura dos boxplots diz que mínimo de noites e avaliações “variam entre tipos”, sem explicitar direção, dimensão ou quais tipos. | Descrever que há diferenças é menos informativo que explicar o padrão concreto mostrado. | Relacionar cada resultado aos valores observados, unidades, sentido e limite da conclusão. |
| Justificativas parcialmente implícitas | A seção 8 apresenta mediana, moda e padronização, mas poderia ligar cada escolha mais diretamente à auditoria e ao estimador futuro. | Um pipeline correto pode ter fundamentação insuficiente para o nível mais alto da rubrica. | Explicitar ausência estrutural, função da padronização no Ridge e razão para manter o mesmo preparo na floresta. |
| Legibilidade e omissões visuais | O histograma de preço na escala original é comprimido pelos extremos; os boxplots de preço usam `showfliers=False` sem avisar nos próprios títulos. Alguns histogramas mantêm o eixo padrão `Count`. | O leitor precisa saber o que foi omitido e conseguir interpretar a figura sem examinar o código. | Mostrar todos os anúncios nos dispersogramas, identificar ampliações e manter unidades e definição do resíduo. |
| Hipóteses sem desfecho explícito | A APS1 propõe `log1p(price)` e análise da redundância geográfica para a etapa seguinte. | O leitor pode entender uma possibilidade como compromisso ou resultado já validado. | Declarar quais hipóteses foram testadas e quais continuam em aberto. |
| Evidência formal de rubrica | O checklist registra todos os itens como atendidos; não substitui a revisão de cada argumento. | Quantidade de gráficos ou presença de PCA, por si só, não mede profundidade. | Mapear requisitos a seções, resultados e ressalvas, sem prometer nota. |

**O que não foi identificado como erro:** o target é contínuo, portanto não faz sentido criar classes artificiais apenas para falar de balanceamento; excluir IDs das estatísticas quantitativas é justificável; preservar extremos plausíveis, ajustar transformadores no treino e usar PCA como diagnóstico também são decisões defensáveis. O enunciado contém exemplos de classificação, mas admite regressão. Não é possível converter automaticamente 8,5 em um conceito específico sem a regra de conversão do professor.

**Exemplo de como aprofundar a interpretação:** no treino da APS1, a mediana de mínimo de noites é 3 para acomodação inteira, 2 para quarto privado e 1 para compartilhado. A disponibilidade mediana vai de 28 dias no Brooklyn a 231,5 em Staten Island. Esses números, recalculados no mesmo split, tornam a descrição concreta; a diferença continua sendo associativa e não demonstra que mudar o tipo de imóvel cause a alteração. Para a APS2, o mesmo cuidado se aplica aos valores dos erros e às contribuições das features.

O limite de gráficos da APS1 admite ambiguidade entre figuras, painéis e variáveis. A versão local usa dois painéis para `price`, além de mínimo de noites e disponibilidade. Isso merece conferência com o professor, mas **não foi classificado como violação comprovada**.

## Riscos concretos corrigidos na APS2

1. **Limitações repetidas.** A discussão final retomava dependência por anfitrião e atribuição entre variáveis correlacionadas, já discutidas anteriormente. Como o enunciado pede limitações adicionais, a seção final agora desenvolve dois pontos do modelo (incerteza individual e extrapolação) e dois dos dados (localização aproximada e atualização dos calendários), com fontes e consequências práticas.
2. **Ganho atribuído ao encoder.** A nova busca é exigida pelo enunciado e foi mantida. Entretanto, a profundidade escolhida também mudou de 20 para 30. O texto agora distingue o resultado após nova otimização do efeito condicional da troca de encoder; uma comparação adicional mantém os hiperparâmetros e mostra os três folds. Nenhum desses diagnósticos reabre a seleção do modelo.
3. **Amostra descrita como distribuição completa.** Os dispersogramas anteriores tinham somente 5.000 dos 9.777 anúncios. Agora mostram todo o teste; a ampliação continua sendo apenas visual, e as métricas continuam com todas as linhas.
4. **Coeficientes sem referência omitida.** O one-hot usa todas as categorias. O coeficiente de Tribeca não é automaticamente um prêmio sobre um bairro de referência. A interpretação agora explica contrastes entre coeficientes e a dependência entre bairro, borough e coordenadas.
5. **Identificador dos exemplos.** As explicações individuais chamavam o índice do DataFrame de anúncio. Agora apresentam o `id` real junto ao índice.
6. **Dispersão inconsistente.** A tabela da curva usava desvio padrão amostral, e a faixa da figura usava o populacional. Ambos agora usam `ddof=1`, identificados como dispersão entre folds, não intervalo de confiança.
7. **Escala e população das explicações.** O notebook explicita numéricas padronizadas no SHAP, contribuições em dólares e ranking global restrito a 200 anúncios. Agrupar contribuições já calculadas não equivale a recalcular SHAP por grupos.
8. **Escolhas pouco justificadas.** Foram acrescentadas razões para a métrica, espaços de busca, três folds e limiar de frequência, sem alegar que sejam ótimos demonstrados.

## Mapa de conferência da APS2

| Requisito do enunciado | Evidência no notebook |
|---|---|
| Mesma preparação inicial da APS1 | Seções 1–2, mesmas features e divisão |
| Dummy, linear regularizado e ensemble | Seção 3, MAE nos mesmos folds |
| Busca para linear e ensemble | Seção 4, espaços e parâmetros vencedores |
| Alteração de pipeline com nova busca | Seção 5, comparação principal e diagnóstico fixo |
| Curva de aprendizado | Seção 6, treino, validação e dispersão |
| Diagnósticos de regressão no teste | Seção 8, três figuras e métricas em dólares |
| Três coeficientes e três importâncias | Seção 9, valores e interpretação contextual |
| SHAP global e três previsões | Seção 10, amostra, unidades e reconstrução |
| Duas limitações novas de cada tipo | Seção 11, modelo e dados separados |
| Duas ações operacionais fundamentadas | Seção 11, aplicação consistente e manutenção |
| Identificação, referências e execução | Capa, bibliografia e saídas do notebook |

## Limites desta revisão

**Validação executada:** 21 células de código, em ordem, sem saídas de erro; notebook e UTF-8 válidos. A reexecução reproduziu MAE 63,076, RMSE 176,741 e R² 0,220 no teste, com a mesma precisão exibida anteriormente. O diagnóstico com parâmetros fixos encontrou delta de MAE de −US$ 0,004 e redução de 234 para 139 colunas. O encerramento do processo em Windows emitiu mensagens do `joblib` sobre limpeza de diretórios temporários; o processo terminou com código zero e salvou todas as saídas. A exportação das nove figuras e a construção estrita do MkDocs foram concluídas.

- O teste já foi consultado na execução original. Reexecutar preserva a reprodutibilidade, mas não cria uma avaliação independente nova. O vencedor, os espaços de busca e a regra de seleção foram mantidos.
- A redução de aproximadamente US$ 0,09 após nova otimização não sustenta uma promessa de melhoria relevante. Três folds sobrepostos também não devem ser tratados como três experimentos independentes.
- A validação por anfitrião usa parâmetros escolhidos na validação aleatória. É um diagnóstico condicional, não substitui seleção e avaliação inteiramente por grupos.
- `log1p(price)`, remoção de redundância geográfica e estabilidade do ranking SHAP continuam sem avaliação nesta entrega. Nenhuma conclusão de superioridade foi acrescentada para essas alternativas.
- O [site da disciplina](https://insper.github.io/ML/pt/2026.2/project/) informa prazo de 30/10, enquanto o Colab conserva 26/10. A capa informa a data da revisão; não declara que o formulário foi enviado.
- A entrega deve apontar para a versão final do [notebook ou da documentação](notebook.md). O envio pelo formulário da disciplina é uma etapa separada da publicação do material.

## Referências metodológicas

- [Scikit-learn: validação cruzada](https://scikit-learn.org/stable/modules/cross_validation.html), para separar seleção e avaliação.
- [Scikit-learn: OneHotEncoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html), para codificação completa e categorias infrequentes.
- [Scikit-learn: RandomForestRegressor](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestRegressor.html), para folhas, critério e agregação.
- [Inside Airbnb: premissas dos dados](https://insideairbnb.com/data-assumptions/), para localização e atualização dos calendários.
