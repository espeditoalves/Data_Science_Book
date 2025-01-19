
- [P Valor](#p-valor)
  - [O que é P VALOR?](#o-que-é-p-valor)
  - [Hipóteses Estatísticas](#hipóteses-estatísticas)
  - [Nível de Significância e Valor de P](#nível-de-significância-e-valor-de-p)
  - [Estatisticamente Significativo?](#estatisticamente-significativo)
  - [O que Significa o Valor de P?](#o-que-significa-o-valor-de-p)

# P Valor

## O que é P VALOR?

O valor de p representa a **probabilidade de a diferença detectada entre os grupos analisados ter ocorrido ao acaso.** 

Então,

– Um **pequeno valor de p** (p ≤ 0,05, ou seja, probabilidade menor ou igual a 5%): 
indica que há uma pequena probabilidade de que a diferença observada entre os grupos seja ao acaso, então, você considera que **`há diferença significativa`** entre os grupos.

– Um **grande valor de p** (p > 0,05, ou seja, probabilidade maior que 5%): 
indica que há uma grande probabilidade de que a diferença observada entre os grupos seja ao acaso, então, você considera que **`não há diferença significativa`** entre os grupos.

Na explicação acima, usamos **“diferença entre os grupos”** como exemplo, que se aplica a análises como **teste t** e **Anova**.

Para testes como correlação de Pearson e regressão linear, passaríamos a dizer **“relação entre as variáveis”**.

**Referência:** https://estatisticafacil.org/2020/10/06/valor_de_p/

> ### Atente-se para a informação a seguir:

> As definições, entendimentos e explicações que utilizamos aqui, são os mais gerais e amplamente utilizadas em disciplinas básicas de estatística ou bioestatística e livros texto.

> Sendo assim, nestes moldes, de forma geral, o entendimento dos significados se torna mais fácil e lógico para quem não é ligado diretamente com a área de exatas.

> Este entendimento, no entanto, vem sendo criticado por alguns estatísticos e, por conta disto, a *Associação Americana de Estatística* publicou um editorial sobre a **`“significância estatística e o valor de p”`**, com aspectos um pouco diferentes dos retratados aqui.

> Abaixo, uma definição mais precisa, mas ao mesmo tempo menos intuitiva.

>>**O valor de p representa a probabilidade de obtermos um resultado igual (ou mais extremo) ao obtido a partir dos nossos dados, assumindo que a hipótese nula é verdadeira.**

Essa definição será discutida nos tópicos abaixo

## Hipóteses Estatísticas

Quando fazemos um **teste inferencial** de hipóteses — como qui-quadrado, teste t, anova, correlação, regressão, etc — temos basicamente duas hipóteses:

 - **HIPÓTESE nula (H0):** A padrão, mais simples, de que não há ‘diferença entre os grupos’ ou não há ‘relação entre as variáveis’.

- **HIPÓTESE alternativa (H1):** Estado alternativo, complementar a H0, de que há ‘diferenças entre grupos’ ou há ‘relação entre as variáveis’.

## Nível de Significância e Valor de P

O **objetivo** básico de todo e qualquer teste de hipóteses é definir se rejeitaremos ou não a hipótese nula (H0) — e essa definição dependerá de dois fatores fundamentais:

**1. NÍVEL DE SIGNIFICÂNCIA (*α*)**

Representa um valor de corte, um critério que definimos para rejeitar H0 ou não. A definição de seu valor — normalmente 1% ou 5% — deve ser feita anteriormente ao teste.

**2. VALOR DE P (p)**

O valor de p representa uma probabilidade, e esse valor será obtido sempre que executarmos um teste inferencial de hipóteses.


## Estatisticamente Significativo?

Ao executar nossa análise e obtermos o valor de p, o próximo passo será compará-lo com o nível de significância (**α**) que definimos anteriormente.

Como exemplo, considere que definimos um nível de significância **(α) de 0,05 (ou 5%)**, teríamos então duas possibilidades ao compararmos esse α com nosso valor de p obtido no teste:

1. Quando o valor de p é menor ou igual ao nível de significância α **`(p ≤ 0,05)`**, devemos então **`rejeitar`** a **`hipótese nula (H0)`**. Aqui dizemos que nosso teste foi **`estatisticamente significativo`**.

2. Quando o valor de p é maior que o nível de significância α **`(p > 0,05)`**, devemos então **`não rejeitar`** a **`hipótese nula (H0)`**. Aqui dizemos que nosso teste **`não foi estatisticamente significativo`**.

## O que Significa o Valor de P?

Em termos técnicos o valor de p pode ser definido como:

> A probabilidade de obtermos um resultado igual (ou mais  extremo)
> ao obtido a partir dos nossos dados, assumindo que a hipótese nula é verdadeira.

Se meu teste retornou, por exemplo, p = 2%, o que isso significa?

Se considerarmos H0 verdadeira, a probabilidade de obtermos resultados iguais (ou mais extremos) que o nosso, será de apenas 2%. Como foi menor que o α = 5%, rejeitamos H0. Veja a seguir.

**Referência:** https://estatisticafacil.org/2022/02/18/valor_de_p_retorno/

