import random
import collections

########### FUNCOES ###########

def fitness(individuo,pesos, valores):
    avalPeso = 0
    avalValor = 0
    #calculando peso total de cada indiv
    for i in range(0,tamanhoInd):
        avalPeso += pesos[i]*individuo[i]
    if(avalPeso > PesoMaximo):
        while(avalPeso > PesoMaximo):
            itemTirado = random.randint(0,tamanhoInd-1)
            if(individuo[itemTirado] == 1):
                individuo[itemTirado] = 0
                avalPeso = avalPeso - pesos[itemTirado]

#calculando peso total
    for i in range(0, tamanhoInd):
        avalValor += valores[i]*individuo[i]

    return avalValor

def pop_fitness(populacao,pesos, valores, tamanhoPop):
    fitnessGeral = []

    for i in range(0, tamanhoPop):
        fitnessGeral.append(fitness(populacao[i], pesos, valores))

    return fitnessGeral

def selecao(fitnessPop, populacao):
    soma = 0
    parentes = []
    for i in range(0, 10):
        limit = random.randint(0,tamanhoPop)
        for j in range(0, tamanhoPop):
            soma += fitnessPop[j]
            if(soma >= limit):
                parentes.append(populacao[j])
                soma = 0
                break

    return parentes

def crossover_simples(parentes):
    filhos = []
    filho1 = []
    filho2 = []
    for i in range(0, len(parentes) - 1, 2):
        ponto = random.randint(0, tamanhoInd)
        filho1 = parentes[i][0:ponto+1] + parentes[i+1][ponto:-1]
        filho2 = parentes[i+1][0:ponto+1] + parentes[i][ponto:-1]

        filhos.append(filho1)
        filhos.append(filho2)

    return filhos

def mutacao(filhos):
    for i in range(0, len(filhos)):
        for j in range(0, tamanhoInd):
            taxaMut = random.randint(0,10)
            if(taxaMut == 1):
                if(filhos[i][j] == 1):
                    filhos[i][j] = 0
                else:
                    filhos[i][j] = 1
    return filhos

def reinsercao(populacao, fitnessPop, filhos, filhos_fit):
    populacao += filhos
    fitnessPop += filhos_fit
    nova_pop = []

    for i in range(0, tamanhoPop):
        fit_max = max(fitnessPop)
        indice = fitnessPop.index(fit_max)
        nova_pop.append(populacao[indice])
        populacao.remove(populacao[indice])
        fitnessPop.remove(fit_max)
    return nova_pop

def criterio_parada(fitnessPop, populacao):
    contadorDeFit = collections.Counter(fitnessPop)
    fitCromFinal = -1
    print(contadorDeFit.values())
    frequenciaValores = list(contadorDeFit.values())
    #Verificando se h algum valor de fit com 90% ou mais de frequencia
    for i in range (0, len(frequenciaValores)):
        if(frequenciaValores[i] >= 0.9*(tamanhoPop)):
                chaves_dic = list(contadorDeFit.keys())
                fitCromFinal = chaves_dic[i]
        #Busca o valor de fit no vetor de fitness da populao
        if(fitCromFinal == -1):
            return -1
        else:
            for i in range (0, tamanhoPop):
                if(fitnessPop[i] == fitCromFinal):
                    return i

############## END FUNCOES #########

#Definir pesos e valores
pesos = [4, 6, 2, 7, 9, 8]
valores = [5,8, 1, 4, 10, 3]

PesoMaximo = 11

#Definir numero de iteres
geracaoMax = 10

#Definir tamanho da populao
tamanhoPop = 50
tamanhoInd = 6

#Definir populao
populacao = []
fitnessPop = []

for i in range(0, tamanhoPop):
    individuo = [random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1), random.randint(0,1)]
    populacao.append(individuo)

fitnessPop = pop_fitness(populacao, pesos, valores, tamanhoPop)


parada = -1
geracao = 0

while(parada == -1 and geracao <= geracaoMax):

    parentes = selecao(fitnessPop, populacao)

    filhos = crossover_simples(parentes)

    filhos = mutacao(filhos)

    fitnessFilho = pop_fitness(filhos, pesos, valores, len(filhos))

    populacao = reinsercao(populacao, fitnessPop, filhos, fitnessFilho)

    fitnessPop = pop_fitness(populacao,pesos,valores,tamanhoPop)

    parada = criterio_parada(fitnessPop,populacao)
    geracao += 1

print(populacao[parada])
print(fitnessPop[parada])
