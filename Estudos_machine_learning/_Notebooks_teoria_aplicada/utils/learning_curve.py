# data analysis and wrangling
import pandas as pd
import numpy as np
import random as rnd

# visualization
import seaborn as sns
import matplotlib.pyplot as plt

#machine learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
from sklearn.model_selection import GridSearchCV

#Learning curve
from sklearn.model_selection import learning_curve
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_predict
from sklearn.model_selection import validation_curve

# Funções para type hints
from typing import Any, Dict, Union, List, Optional, Tuple
from sklearn.base import BaseEstimator


def grid_search_model(X: np.ndarray, 
                      Y: np.ndarray, 
                      model: BaseEstimator, 
                      parameters: Dict[str, Any], 
                      cv: Union[int, Any]) -> None:
    """
    Realiza uma busca em grade para encontrar os melhores hiperparâmetros para um modelo de Machine Learning.

    Args:
        X (np.ndarray): Dados de entrada (features) para o treinamento.
        Y (np.ndarray): Dados de saída (rótulos) para o treinamento.
        model (BaseEstimator): O modelo de Machine Learning a ser treinado.
        parameters (Dict[str, Any]): Dicionário de parâmetros a serem testados na busca em grade.
        cv (Union[int, Any]): Número de folds para a validação cruzada ou um objeto de gerador de validação cruzada.

    Returns:
        None: A função imprime o melhor score e os melhores parâmetros encontrados.
    """
    CV_model = GridSearchCV(estimator=model, param_grid=parameters, cv=cv)
    CV_model.fit(X, Y)
    print("Best Score:", CV_model.best_score_, " / Best parameters:", CV_model.best_params_)

 # Usar BaseEstimator como type hint significa que você pode passar qualquer 
 # modelo de aprendizado de máquina do scikit-learn para a função, 
 # seja ele uma regressão linear, uma árvore de decisão, uma máquina de vetores de suporte (SVM), uma rede neural, etc.


# validacion curv
def validation_curve_model(X: np.ndarray, 
                           Y: np.ndarray, 
                           model: BaseEstimator, 
                           param_name: str, 
                           parameters: List[Any], 
                           cv: Union[int, Any], 
                           ylim: Optional[Tuple[float, float]] = None, 
                           log: bool = True) -> plt.Figure:
    """
    Plota a curva de validação para um modelo de Machine Learning, mostrando o desempenho de treinamento e validação.

    Args:
        X (np.ndarray): Dados de entrada (features) para o treinamento.
        Y (np.ndarray): Dados de saída (rótulos) para o treinamento.
        model (BaseEstimator): O modelo de Machine Learning a ser avaliado.
        param_name (str): Nome do hiperparâmetro a ser testado.
        parameters (List[Any]): Lista de valores para o hiperparâmetro.
        cv (Union[int, Any]): Número de folds para a validação cruzada ou um objeto de gerador de validação cruzada.
        ylim (Optional[Tuple[float, float]]): Limites para o eixo y no gráfico (opcional).
        log (bool): Se verdadeiro, usa escala logarítmica para o eixo x.

    Returns:
        plt.Figure: O objeto de figura do matplotlib contendo a curva de validação.
    """
    train_scores, test_scores = validation_curve(
        model, X, Y, param_name=param_name, param_range=parameters, cv=cv, scoring="accuracy"
    )
    
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)

    plt.figure()
    plt.title("Curva de Validação")
    plt.fill_between(parameters, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(parameters, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")

    if log:
        plt.semilogx(parameters, train_scores_mean, 'o-', color="r", label="Pontuação de Treinamento")
        plt.semilogx(parameters, test_scores_mean, 'o-', color="g", label="Pontuação de Validação Cruzada")
    else:
        plt.plot(parameters, train_scores_mean, 'o-', color="r", label="Pontuação de Treinamento")
        plt.plot(parameters, test_scores_mean, 'o-', color="g", label="Pontuação de Validação Cruzada")

    if ylim is not None:
        plt.ylim(*ylim)

    plt.ylabel('Pontuação')
    plt.xlabel(f'Parâmetro {param_name}')
    plt.legend(loc="best")

    return plt

# Learning curve
def Learning_curve_model(X: np.ndarray, 
                         Y: np.ndarray, 
                         model: BaseEstimator, 
                         cv: Union[int, Any], 
                         train_sizes: Union[np.ndarray, List[int]]) -> plt.Figure:
    """
    Plota a curva de aprendizado para um modelo de Machine Learning, mostrando o desempenho de treinamento e validação
    em diferentes tamanhos de conjunto de treinamento.

    Args:
        X (np.ndarray): Dados de entrada (features) para o treinamento.
        Y (np.ndarray): Dados de saída (rótulos) para o treinamento.
        model (BaseEstimator): O modelo de Machine Learning a ser avaliado.
        cv (Union[int, Any]): Número de folds para a validação cruzada ou um objeto de gerador de validação cruzada.
        train_sizes (Union[np.ndarray, List[int]]): Tamanhos dos conjuntos de treinamento a serem usados para gerar a curva de aprendizado.

    Returns:
        plt.Figure: O objeto de figura do matplotlib contendo a curva de aprendizado.
    """
    plt.figure()
    plt.title("Curva de Aprendizado")
    plt.xlabel("Exemplos de Treinamento")
    plt.ylabel("Pontuação")

    train_sizes, train_scores, test_scores = learning_curve(model, X, Y, cv=cv, n_jobs=4, train_sizes=train_sizes)

    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std  = np.std(train_scores, axis=1)
    test_scores_mean  = np.mean(test_scores, axis=1)
    test_scores_std   = np.std(test_scores, axis=1)
    plt.grid()
    
    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1, color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r", label="Pontuação de Treinamento")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g", label="Pontuação de Validação Cruzada")
                     
    plt.legend(loc="best")
    return plt

# lrearning, prediction and printing results
def predict_model(X: np.ndarray, 
                  Y: np.ndarray, 
                  model: BaseEstimator, 
                  Xtest: np.ndarray, 
                  submit_name: str, 
                  test_df: pd.DataFrame, 
                  cv: Union[int, Any] = 5) -> np.ndarray:
    """
    Treina o modelo, faz previsões e salva os resultados em um arquivo CSV.

    Args:
        X (np.ndarray): Dados de entrada (features) para o treinamento.
        Y (np.ndarray): Dados de saída (rótulos) para o treinamento.
        model (BaseEstimator): O modelo de Machine Learning a ser treinado.
        Xtest (np.ndarray): Dados de entrada (features) para o teste.
        submit_name (str): Nome do arquivo CSV para salvar as previsões.
        test_df (pd.DataFrame): DataFrame contendo os dados de teste, incluindo o 'PassengerId'.
        cv (Union[int, Any], optional): Número de folds para a validação cruzada ou um objeto de gerador de validação cruzada. Default é 5.

    Returns:
        np.ndarray: Array contendo as pontuações de validação cruzada.
    """
    model.fit(X, Y)
    Y_pred = model.predict(Xtest)
    score = cross_val_score(model, X, Y, cv=cv)

    submission = pd.DataFrame({
        "PassengerId": test_df["PassengerId"],
        "Survived": Y_pred
    })
    submission.to_csv(submit_name, index=False)
    
    return score