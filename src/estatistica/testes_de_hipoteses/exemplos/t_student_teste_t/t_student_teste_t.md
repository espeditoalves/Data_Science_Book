{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "# Teste T Pareado: Cálculo Manual\n",
    "\n",
    "Este documento explica como realizar um teste t pareado manualmente para determinar se há uma diferença significativa entre as médias de duas amostras emparelhadas. Neste exemplo, utilizamos duas colunas de dados representando métricas de KS scores.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Dados\n",
    "\n",
    "Vamos utilizar os seguintes dados:\n",
    "\n",
    "- `ks.scores1`: [0.583983, 0.576596, 0.556730, 0.595138, 0.584564]\n",
    "- `ks.scores2`: [0.490242, 0.551584, 0.514383, 0.535587, 0.546064]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "## Passo a Passo para o Teste T Pareado Manualmente\n",
    "\n",
    "### 1. Calcular as Diferenças\n",
    "\n",
    "Primeiro, calculamos a diferença entre as duas colunas para cada par de valores:\n",
    "\n",
    "$$\n",
    "\\text{Diferença} = \\text{ks.scores1} - \\text{ks.scores2}\n",
    "$$\n",
    "\n",
    "\n",
    "$$ \\begin{align*} \n",
    "0.583983 - 0.490242 &= 0.093741\\\\\\\\\n",
    "0.576596 - 0.551584 &= 0.025012\\\\\\\\\n",
    "0.556730 - 0.514383 &= 0.042347\\\\\\\\\n",
    "0.595138 - 0.535587 &= 0.059551\\\\\\\\\n",
    "0.584564 - 0.546064 &= 0.038500\\\\\\\\\n",
    "\\end{align*}\n",
    "$$\n",
    "\n",
    "\n",
    "\n",
    "Então, as diferenças são:\n",
    "\n",
    "$$\n",
    "\\text{Diferenças} = [0.093741, 0.025012, 0.042347, 0.059551, 0.038500]\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### 2. Calcular a Média das Diferenças\n",
    "\n",
    "Agora, calculamos a média das diferenças ($\\bar{d}$):\n",
    "\n",
    "$$\n",
    "\\bar{d} = \\frac{1}{n} \\sum_{i=1}^{n} d_i = \\frac{0.093741 + 0.025012 + 0.042347 + 0.059551 + 0.038500}{5}\n",
    "$$\n",
    "\n",
    "$$\n",
    "\\bar{d} = \\frac{0.259151}{5} = 0.0518302\n",
    "$$\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 3. Calcular o Desvio Padrão das Diferenças\n",
    "\n",
    "Para calcular o desvio padrão ($s_d$), usamos a fórmula do desvio padrão de uma amostra:\n",
    "\n",
    "$$\n",
    "s_d = \\sqrt{\\frac{\\sum_{i=1}^{n} (d_i - \\bar{d})^2}{n-1}}\n",
    "$$\n",
    "\n",
    "$$\n",
    "\\begin{align*}\n",
    "(d_1 - \\bar{d})^2 &= (0.093741 - 0.0518302)^2 = 0.001749 \\\\\\\\\n",
    "(d_2 - \\bar{d})^2 &= (0.025012 - 0.0518302)^2 = 0.000712 \\\\\\\\\n",
    "(d_3 - \\bar{d})^2 &= (0.042347 - 0.0518302)^2 = 0.000090 \\\\\\\\\n",
    "(d_4 - \\bar{d})^2 &= (0.059551 - 0.0518302)^2 = 0.000059 \\\\\\\\\n",
    "(d_5 - \\bar{d})^2 &= (0.038500 - 0.0518302)^2 = 0.000177 \\\\\\\\\n",
    "\\end{align*}\n",
    "$$\n",
    "\n",
    "Agora, somamos essas diferenças quadradas e dividimos pelo número de pares menos um:\n",
    "\n",
    "$$\n",
    "\\sum (d_i - \\bar{d})^2 = 0.001749 + 0.000712 + 0.000090 + 0.000059 + 0.000177 = 0.002787\n",
    "$$\n",
    "\n",
    "$$\n",
    "s_d = \\sqrt{\\frac{0.002787}{5-1}} = \\sqrt{\\frac{0.002787}{4}} = \\sqrt{0.00069675} = 0.026396\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### 4. Calcular a Estatística t\n",
    "\n",
    "A estatística t é calculada usando a média das diferenças, o desvio padrão das diferenças e o número de pares:\n",
    "\n",
    "$$\n",
    "t = \\frac{\\bar{d}}{s_d / \\sqrt{n}}\n",
    "$$\n",
    "\n",
    "Onde:\n",
    "- ($\\bar{d}$) é a média das diferenças.\n",
    "- ($s_d$) é o desvio padrão das diferenças.\n",
    "- ($n$) é o número de pares.\n",
    "\n",
    "Substituindo os valores:\n",
    "\n",
    "$$\n",
    "t = \\frac{0.0518302}{0.026396 / \\sqrt{5}} = \\frac{0.0518302}{0.011804} = 4.389\n",
    "$$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### 5. Determinar o Valor p\n",
    "\n",
    "Para determinar o valor p, utilizamos a tabela de distribuição t de Student. Com $n - 1 = 4$ graus de liberdade e uma estatística $t$ de $4.389$, vamos buscar o valor p correspondente.\n",
    "\n",
    "- Para $t = 4.389$ e $df = 4$, o valor p é geralmente menor que $0.05$, indicando que existe uma diferença significativa.\n",
    "\n",
    "### 5.1 Determinar a Região Crítica\n",
    "Para um teste t, a região crítica depende do nível de significância ($𝛼$) e do tipo de teste (unilateral ou bilateral). Para um teste t bilateral, a região crítica está nas duas extremidades da distribuição t.\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "### **Exemplo Prático**\n",
    "\n",
    "- **Localize a estatística t calculada:** 4.389\n",
    "- **Localize a coluna com o nível de significância desejado** (por exemplo, $𝛼=0.05$ para um teste de duas caudas).\n",
    "- **Compare o valor da estatística t com os valores críticos da tabela:**\n",
    "\n",
    "    Para $𝛼=0.05$ em um teste de duas caudas e 4 graus de liberdade, o valor crítico geralmente é cerca de 2.776.\n",
    "    Como $t=4.389$ é maior que o valor crítico de 2.776, isso indica que a estatística t está na região crítica e o valor p é menor que 0.05.\n",
    "\n",
    ">**Se a sua estatística t calculada (t = 4.389) exceder o valor crítico da tabela t para o nível de significância escolhido, `você rejeita a hipótese nula`. Para testes de duas caudas, você precisa comparar a estatística t com o valor crítico para a região crítica em ambas as extremidades da distribuição.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Conclusão\n",
    "\n",
    "- **Valor de t calculado:** 4.389\n",
    "- **Graus de liberdade (df):** 4\n",
    "- **Valor p:** Aproximadamente $0.0053$ (menor que $0.05$)\n",
    "\n",
    "Com base nos cálculos, **`podemos rejeitar a hipótese nula`** e concluir que existe uma diferença significativa entre as médias das métricas `ks.scores1` e `ks.scores2`.\n",
    "\n",
    "### Resumo do Teste T Pareado:\n",
    "\n",
    "- **Hipótese Nula (H0):** A diferença entre as médias das métricas é zero.\n",
    "- **Hipótese Alternativa (H1):** A diferença entre as médias das métricas não é zero.\n",
    "- **Resultado:** **`Rejeitamos a hipótese nula`**. Existe uma diferença significativa entre as médias das métricas.\n",
    "---\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Teste T Pareado usando Python**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Para testar se existe uma diferença significativa entre as médias das métricas das duas colunas \n",
    "**`ks.scores1`** e **`ks.scores2`**, podemos usar um **`teste t pareado`**. \n",
    "Este teste é adequado para comparar as médias de duas amostras emparelhadas, \n",
    "assumindo que as diferenças entre as amostras seguem uma distribuição normal."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### **Passos para realizar o Teste T Pareado:**\n",
    "\n",
    "**1. Formulação das Hipóteses:**\n",
    "\n",
    "- **`H0 (Hipótese Nula):`** A diferença entre as médias das métricas é zero ($𝜇_1 −𝜇_2 = 0$).\n",
    "- **`H1 (Hipótese Alternativa):`** A diferença entre as médias das métricas não é zero ($𝜇_1 −𝜇_2$ != $0$).\n",
    "\n",
    "**2. Cálculo da Diferença das Métricas:**\n",
    "\n",
    "- Para cada par de valores das duas colunas, calcule a diferença.\n",
    "\n",
    "**3. Aplicação do Teste T Pareado:**\n",
    "\n",
    "- Utilize a diferença calculada para aplicar o **`teste t pareado`**.\n",
    "- Calcule o **`valor p`** para determinar se as diferenças são estatisticamente significativas."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## **Implementação em Python:**\n",
    "\n",
    "Vou demonstrar como você pode implementar isso usando a biblioteca **`scipy.stats`** para calcular o **teste t pareado**."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Estatística t: 4.378132332736648\n",
      "Valor p: 0.011892242763488443\n",
      "Rejeitamos a hipótese nula: Há diferença significativa entre as médias.\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from scipy import stats\n",
    "\n",
    "# Dados fornecidos: ks.scores\n",
    "data = {\n",
    "    \"ks.scores1\": [0.583983, 0.576596, 0.556730, 0.595138, 0.584564],\n",
    "    \"ks.scores2\": [0.490242, 0.551584, 0.514383, 0.535587, 0.546064]\n",
    "}\n",
    "\n",
    "# Criar o DataFrame\n",
    "df = pd.DataFrame(data)\n",
    "\n",
    "# Calcular o teste T pareado\n",
    "t_statistic, p_value = stats.ttest_rel(df['ks.scores1'], df['ks.scores2'])\n",
    "\n",
    "# Exibir resultados\n",
    "print(\"Estatística t:\", t_statistic)\n",
    "print(\"Valor p:\", p_value)\n",
    "\n",
    "# Avaliação do resultado\n",
    "if p_value < 0.05:\n",
    "    print(\"Rejeitamos a hipótese nula: Há diferença significativa entre as médias.\")\n",
    "else:\n",
    "    print(\"Não rejeitamos a hipótese nula: Não há diferença significativa entre as médias.\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
