# Qualidade, extremos e vieses

## Ausências e consistência

| Variável | Ausências | Interpretação |
|---|---:|---|
| name | 16 | Campo textual fora do baseline |
| host_name | 21 | Campo textual fora do baseline |
| last_review | 10.052 | Ausência estrutural sem avaliações |
| reviews_per_month | 10.052 | Ausência estrutural sem avaliações |

Todas as ausências de `last_review` e `reviews_per_month` coincidem com anúncios
sem avaliações. Não há casos ausentes dessas colunas quando
`number_of_reviews` é maior que zero.

**Decisão:** preencher `reviews_per_month` com zero apenas para anúncios sem
avaliações e criar `has_reviews`. A data bruta fica fora do baseline.

## Outliers investigados

O percentil 99 de preço no treino é **US$ 798,76**, com 392 anúncios acima desse
limite. Os maiores preços chegam a US$ 9.999–10.000. O maior mínimo de noites é
1.250 e a maior escala observada de anfitrião é 327 anúncios.

| Situação | Leitura | Decisão |
|---|---|---|
| 11 preços não positivos | Violam a definição do target | Remover |
| Preços de até US$ 10.000 | Extremos plausíveis | Manter e testar |
| Mínimos de até 1.250 noites | Possíveis contratos longos | Monitorar |
| Anfitriões com 327 anúncios | Compatível com operador profissional | Manter |

### Critério de tratamento

Valores extremos não foram removidos apenas por distância estatística. A
decisão distingue valores inválidos de observações incomuns mas plausíveis.

## Vieses e representatividade

| Borough | Participação no treino |
|---|---:|
| Manhattan | 44,4% |
| Brooklyn | 41,1% |
| Queens | 11,6% |
| Bronx | 2,2% |
| Staten Island | 0,7% |

Manhattan e Brooklyn representam **85,5%** do treino. Métricas agregadas refletem
principalmente esses grupos, e conclusões sobre Bronx e Staten Island têm menor
suporte amostral.

Outros riscos:

- **Seleção:** aparecem apenas anúncios presentes no Airbnb neste recorte.
- **Sobrevivência:** anúncios removidos ou inativos podem estar ausentes.
- **Avaliações:** dependem de reserva e da decisão do hóspede de avaliar.
- **Variáveis omitidas:** faltam tamanho, comodidades, taxas e estado do imóvel.
- **Temporalidade:** os dados são históricos e não representam o mercado atual.

Na APS2, o erro deverá ser analisado também por borough e tipo de acomodação.
