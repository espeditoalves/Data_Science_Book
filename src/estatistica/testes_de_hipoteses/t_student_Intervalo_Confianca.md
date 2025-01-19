
- [Cálculo de Intervalo de Confiança Usando t-Student](#cálculo-de-intervalo-de-confiança-usando-t-student)
  - [Dados Fornecidos](#dados-fornecidos)
  - [Passo 1: Calcular a Média Amostral ($\\bar{x}$)](#passo-1-calcular-a-média-amostral-barx)
  - [Passo 2: Calcular o Desvio Padrão Amostral ($s$)](#passo-2-calcular-o-desvio-padrão-amostral-s)
  - [Passo 3: Calcular o Intervalo de Confiança](#passo-3-calcular-o-intervalo-de-confiança)
    - [Entendendo o $𝛼$](#entendendo-o-𝛼)
    - [Divisão de $𝛼$ entre as Caudas](#divisão-de-𝛼-entre-as-caudas)
    - [Escolha do valor de $t\_{\\alpha/2, n-1}$](#escolha-do-valor-de-t_alpha2-n-1)
  - [Resultado Final](#resultado-final)
  - [Interpretação do Intervalo de Confiança](#interpretação-do-intervalo-de-confiança)
    - [1. Significado do Intervalo de Confiança](#1-significado-do-intervalo-de-confiança)
    - [2. Nível de Confiança de 95%](#2-nível-de-confiança-de-95)
    - [3. Interpretação do Erro Padrão da Média (SEM)](#3-interpretação-do-erro-padrão-da-média-sem)
    - [4. Precisão da Estimativa](#4-precisão-da-estimativa)
  - [Interpretação Generica do Intervalo de Confiança](#interpretação-generica-do-intervalo-de-confiança)

# Cálculo de Intervalo de Confiança Usando t-Student

## Dados Fornecidos

Os dados fornecidos são do *AUC_PR*:

- $x_1 = 0.769682$
- $x_2 = 0.758596$
- $x_3 = 0.762273$
- $x_4 = 0.776236$
- $x_5 = 0.760402$


## Passo 1: Calcular a Média Amostral ($\bar{x}$)

A média amostral ## Passo 1: Calcular a Média Amostral ($\bar{x}$) é calculada somando todos os valores e dividindo pelo número total de observações ($n$):

$$
\bar{x} = \frac{x_1 + x_2 + x_3 + x_4 + x_5}{5}
$$

$$
\bar{x} = \frac{0.769682 + 0.758596 + 0.762273 + 0.776236 + 0.760402}{5}
$$

$$
\bar{x} = \frac{3.827189}{5}
$$

$$
\bar{x} = 0.765438
$$


## Passo 2: Calcular o Desvio Padrão Amostral ($s$)

Para calcular o desvio padrão amostral, utilizamos a fórmula:

$$
s = \sqrt{\frac{\sum_{i=1}^{n}(x_i - \bar{x})^2}{n - 1}}
$$

Primeiro, calculamos cada termo $(x_i - \bar{x})^2$:

- $(x_1 - \bar{x})^2 = (0.769682 - 0.765438)^2 = 0.00001806$
- $(x_2 - \bar{x})^2 = (0.758596 - 0.765438)^2 = 0.00004683$
- $(x_3 - \bar{x})^2 = (0.762273 - 0.765438)^2 = 0.00000998$
- $(x_4 - \bar{x})^2 = (0.776236 - 0.765438)^2 = 0.00011589$
- $(x_5 - \bar{x})^2 = (0.760402 - 0.765438)^2 = 0.00002534$


Agora, somamos os quadrados das diferenças:

$$
\sum_{i=1}^{n}(x_i - \bar{x})^2 = 0.00001806 + 0.00004683 + 0.00000998 + 0.00011589 + 0.00002534 = 0.0002161
$$

Calculando o desvio padrão amostral (\(s\)):

$$
s = \sqrt{\frac{0.0002161}{5 - 1}} = \sqrt{\frac{0.0002161}{4}} = \sqrt{0.00005403} \approx 0.00735
$$


## Passo 3: Calcular o Intervalo de Confiança

O intervalo de confiança para a média de uma amostra, usando a distribuição **`t-Student`**, é dado por:

$$
IC = \bar{x} \pm t_{\alpha/2, n-1} \cdot \frac{s}{\sqrt{n}}
$$

### Entendendo o $𝛼$

Para um intervalo de confiança de 95%, o valor de  $𝛼$ representa a probabilidade de erro, ou seja, a área das caudas da distribuição **`t-Student`** que não é coberta pelo intervalo de confiança. Neste caso, $𝛼=1−0.95=0.05$, ou 5%. Isso significa que há uma chance de 5% de que a média verdadeira não esteja dentro do intervalo calculado.

### Divisão de $𝛼$ entre as Caudas

Como o intervalo de confiança é simétrico em torno da média amostral, o valor de $𝛼$ é dividido igualmente entre as duas caudas da distribuição. Portanto, cada cauda tem uma área de $𝛼/2=0.025$.

### Escolha do valor de $t_{\alpha/2, n-1}$

O valor de $t_{\alpha/2, n-1}$ é obtido da tabela t-Student para $n−1=4$ graus de liberdade, correspondendo a uma cauda de 2.5% em cada lado da distribuição. O valor típico para um nível de confiança de 95% e 4 graus de liberdade é aproximadamente 2.776.

Substituindo os valores:

- $\bar{x} = 0.765438$
- $s = 0.00735$
- $n = 5$
- $t_{0.025, 4} \approx 2.776$


O erro padrão da média (SEM) é calculado como:

$$
\frac{s}{\sqrt{n}} = \frac{0.00735}{\sqrt{5}} = \frac{0.00735}{2.236} \approx 0.003285
$$

- $s$: Desvio padrão da amostra, que mede a dispersão dos dados em relação à média amostral.
- $𝑛$: Tamanho da amostra, ou seja, o número total de observações na amostra.

Agora, calculamos o intervalo de confiança:

$$
IC = 0.765438 \pm 2.776 \times 0.003285
$$

$$
IC = 0.765438 \pm 0.009113
$$

$$
IC = [0.756325, 0.774551]
$$

## Resultado Final

O intervalo de confiança de 95% para os dados fornecidos é aproximadamente:

$$
IC = [0.756325, 0.774551]
$$

Ou seja, com 95% de confiança, podemos afirmar que a média verdadeira dos dados está entre 0.756325 e 0.774551.

## Interpretação do Intervalo de Confiança

### 1. Significado do Intervalo de Confiança

- Intervalo Calculado: $[0.756325,0.774551]$.

    Isso significa que, com 95% de confiança, a média verdadeira da população da qual a amostra foi retirada está entre 0.756325 e 0.774551.

- Média Amostral ($\bar{x}$): 0.765438.

    A média amostral é a melhor estimativa pontual da média verdadeira da população. O intervalo de confiança fornece uma faixa ao redor dessa média, refletindo a incerteza da estimativa.

### 2. Nível de Confiança de 95%

O nível de confiança de 95% implica que, se repetíssemos o processo de amostragem muitas vezes (com diferentes amostras do mesmo tamanho), em 95% das vezes, o intervalo calculado conteria a verdadeira média da população.

### 3. Interpretação do Erro Padrão da Média (SEM)

- Erro Padrão da Média (SEM): $0.003285$

    O SEM nos diz o quanto a média amostral ($\bar{x}$) pode variar de uma amostra para outra. Nesse caso, o SEM de $0.003285$ indica que a média das amostras tende a variar em torno de $0.003285$ unidades em relação à média verdadeira da população.

### 4. Precisão da Estimativa
- **Intervalo Estreito:** O intervalo relativamente estreito ($[0.756325,0.774551]$) indica que a estimativa da média amostral é bastante precisa. Isso ocorre porque o desvio padrão é pequeno e o tamanho da amostra é adequado para garantir uma boa estimativa.

- **Implicações Práticas:** Em contextos práticos, como análise financeira ou pesquisa científica, essa precisão significa que podemos confiar que a média da população real está dentro do intervalo calculado com um alto nível de confiança.

## Interpretação Generica do Intervalo de Confiança 

Um intervalo de confiança de 95% para uma média amostral significa que, se coletarmos 100 amostras diferentes e calcularmos um intervalo de confiança para cada uma, esperamos que 95 desses intervalos contenham a verdadeira média da população.