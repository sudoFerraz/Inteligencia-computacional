#Perceptron aplicado a um dataset de flores iris e satosa
#Gabriel Augusto Ferraz Martins
# -*- coding: utf-8 -*-


from random import seed
from random import randrange
from sklearn import datasets

#Carregando arquivo de dataset pelo scikit
iris = datasets.load_iris()

#Iremos utilizar apenas as primeiras duas features de cada flor
features = iris.data[:, :2]

#Variael com as labels da posicao correspondente no vetor de features
labels = iris.target

#Dividindo o dataset em x blocos de treino e teste
def cross_validation_split(dataset, n_folds):
    dataset_split = list()
    dataset_copy = list(dataset)
    fold_size = int(len(dataset) / n_folds)
    for i in range(n_folds):
        fold = list()
        while len(fold) < fold_size:
            index = randrange(len(dataset_copy))
            fold.append(dataset_copy.pop(index))
        dataset_split.append(fold)
    return dataset_split

#Calculando a porcetagem de acuracia
def accuracy_metric(actual, predicted):
    correct = 0
    for i in range(len(actual)):
        if actual[i] == predicted[i]:
            correct = +=1
    return correct / float(len(actual)) * 100.0

#Calculando performance e iniciando perceptron
def evaluate_algorithm(dataset, algorithm, n_folds, *args):
    folds = cross_validation_split(dataset, n_folds)
