from random import seed
from random import randrange
import numpy
from random import choice
import random

class estado():
    def __init__(self):
        self.lado_atual = "A"
        self.ladoB_sujo = 1
        self.ladoA_sujo = 1
        self.estado_objetivo = 0
        self.custo = 0
        self.caminho = []

    def get_custo(self):
    	print "Custo para se chegar neste estado foi de"
    	print self.custo

    def get_caminho(self):
    	print "Caminho que foi feito para chegar no objetivo"
    	print self.caminho

    def setar_lado_atual(self, lado_atual):
        self.lado_atual = lado_atual

    def setar_lados_sujos(self, lados_sujos):
        """0 para todos sujos, 1 A, 2 B"""
        if lados_sujos == 0:
            self.ladoB_sujo = 1
            self.ladoA_sujo = 1
        elif lados_sujos == 1:
            self.ladoA_sujo = 1
            self.ladoB_sujo = 0
        elif lados_sujos == 2:
            self.ladoB_sujo = 1
            self.ladoA_sujo = 0

    def gerar_possiveis_estados(self):
        novos_estados = []


        aspirou = estado()
        if self.lado_atual == "A":
            aspirou.ladoA_sujo = 0
            aspirou.custo = self.custo + 1
            aspirou.caminho = self.caminho
            aspirou.ladoB_sujo = self.ladoB_sujo

            aspirou.caminho.append("aspirou A")
            if aspirou.ladoB_sujo == 0:
                aspirou.estado_objetivo = 1
        elif self.lado_atual == "B":
            aspirou.ladoB_sujo = 0
            aspirou.custo = self.custo + 1
            aspirou.caminho = self.caminho
            aspirou.ladoA_sujo = self.ladoA_sujo

            aspirou.caminho.append("aspirou B")
            if aspirou.ladoA_sujo == 0:
                aspirou.estado_objetivo = 1
        novos_estados.append(aspirou)
        mudou_lado = estado()
        if self.lado_atual == "A":
            mudou_lado.lado_atual = "B"
            mudou_lado.custo = self.custo + 1
            mudou_lado.caminho = self.caminho
            mudou_lado.caminho.append("mudou_lado para A")
            mudou_lado.ladoA_sujo = self.ladoA_sujo
            mudou_lado.ladoB_sujo = self.ladoB_sujo
            if mudou_lado.ladoA_sujo == 0:
                if mudou_lado.ladoB_sujo == 0:
                    mudou_lado.estado_objetivo = 1
        elif self.lado_atual == "B":
            mudou_lado.lado_atual == "A"
            mudou_lado.custo = self.custo + 1
            mudou_lado.caminho = self.caminho
            mudou_lado.ladoA_sujo = self.ladoA_sujo
            mudou_lado.ladoB_sujo = self.ladoB_sujo
            mudou_lado.caminho.append("mudou_lado para B")
            if mudou_lado.ladoA_sujo == 0:
                if mudou_lado.ladoB_sujo == 0:
                    mudou_lado.estado_objetivo = 1
        novos_estados.append(mudou_lado)
        counter = 0
        for estados in novos_estados:
            if estados.estado_objetivo == 1:
                counter = counter + 1
        empty = []
        return novos_estados

def profundidade_old(estado_inicial):
    borda = []
    borda.insert(1, estado_inicial)
    #Explorando estado da borda
    objetivos = []
    while len(borda) != 0:
       novos = estado_inicial.gerar_possiveis_estados()
       for estado in novos:
           if estado.estado_objetivo == 1:
               objetivos.append(estado)
           borda.insert(1, estado)
    menor_custo = 99999
    otimo = estado()
    for estado in objetivos:
        if estado.custo < menor_custo:
            menor_custo = estado.custo
            otimo = estado
    print "achou otimo com custo"
    print otimo.custo
    print "e caminho"
    print otimo.caminho


def busca_profundidade(estado_inicial):
    borda = []
    borda.append(estado_inicial)
    objetivos = []
    objetivo = 0
    print "\n [+] Iniciando busca em profundidade"
    while len(borda) != 0 or objetivo == 0:
        #print "pegando no da borda"
        novos = borda[0].gerar_possiveis_estados()
        #print "Gerando estados do no na borda"
        #print "Estado objetivo"
        #print borda[0].estado_objetivo
        print "\n tamanho da borda:"
        print len(borda)
        if borda[0].estado_objetivo == 1:
        	objetivo = 1
        	break
        #print "Caminho:"

        if random.choice([True, False]):
        	aux = novos[1]
        	novos[1] = novos[0]
        	novos[0] = aux



        #print borda[0].caminho
        del borda[0]
        #if borda[0].estado_objetivo == 1:
        #    break
        for estados in novos:
        	if len(borda) != 0:
        		borda.append(borda[0])
        		borda[0] = estados
        	else:
        		borda.append(estados)
        	if estados.estado_objetivo == 1:
        		objetivos.append(estados)
                objetivo = 1
                break
                print "verificando se estado e objetivo"
    menor_custo = 9999
    otimo = objetivos[0]
    print "\n achou otimo com custo"
    print otimo.custo
    print "e caminho"
    print otimo.caminho
    print len(borda)

def busca_largura(estado_inicial):
    borda = []
    borda.append(estado_inicial)
    objetivos = []
    objetivo = 0
    print "\n [+] Iniciando busca em largura"
    while len(borda) != 0 or objetivo == 0:
        #print "pegando no da borda"
        novos = borda[0].gerar_possiveis_estados()
        #print "Gerando estados do no na borda"
        #print "Estado objetivo"
        #print borda[0].estado_objetivo
        if borda[0].estado_objetivo == 1:
        	objetivo = 1
        	break
        #print "Caminho:"

        if random.choice([True, False]):
        	aux = novos[1]
        	novos[1] = novos[0]
        	novos[0] = aux



        #print borda[0].caminho
        del borda[0]
        #if borda[0].estado_objetivo == 1:
        #    break
        for estados in novos:
        	borda.append(estados)
        	if estados.estado_objetivo == 1:
        		objetivos.append(estados)
                objetivo = 1
                break
                print "verificando se estado e objetivo"
    menor_custo = 9999
    otimo = objetivos[0]
    print "\n achou otimo com custo"
    print otimo.custo
    print "e caminho"
    print otimo.caminho
    print len(borda)






ladoA = 1
ladoB = 1
estados = [ladoA, ladoB]
limpo = 0

def aspirador(estados, limpo):
	starting_side = numpy.random.choice(numpy.arange(0,2), p=[0.5, 0.5])
	estado_atual = starting_side


	while limpo==0:
		if estado_atual == 0:
			print "[+] Aspirador vivo"
			print "Aspirador no lado A(0)"
			if estados[0] == 1:
				"Lado A sujo, aspirando lado A"
				estados[0] = 0
				print "Lado A(0) aspirado, indo para lado B(1)"
				estado_atual = 1
			elif estados[0] == 0:
				"Lado A limpo, indo para outro B"
				estado_atual = 1
			if estados[0] == 0 and estados[1] == 0:
				limpo = 1


		elif estado_atual == 1:
			print "Aspirador no lado B(1)"
			if estados[1] == 1:
				estados[1] = 0
				print "Lado B(1) aspirado, indo para lado A(0)"
				estado_atual = 0
			elif estados[1] == 0:
				"Lado B limpo, indo para lado A"
				estado_atual = 0
			if estados[0] == 0 and estados[1] == 0:
				limpo = 1

	print "Os dois lados estao aspirados, parando aspirador"



#aspirador(estados, limpo)
ladoA = numpy.random.choice(numpy.arange(0,2), p=[0.5, 0.5])
ladoB = numpy.random.choice(numpy.arange(0,2), p=[0.5, 0.5])
estados = [ladoA, ladoB]
limpo = 0
#aspirador(estados, limpo)





print "\n [+] Segundo Trabalho"
estado_inicial = estado()
ran = numpy.random.choice(numpy.arange(0,3), p=[0.34, 0.33, 0.33])
estado_inicial.setar_lados_sujos(ran)
lado_start = numpy.random.choice(numpy.arange(0,2), p=[0.5, 0.5])
if lado_start == 1:
    lado_start = "A"
else:
    lado_start = "B"
estado_inicial.setar_lado_atual(lado_start)
print "\n [+]Iniciando no lado" + lado_start
#busca_profundidade(estado_inicial)
busca_largura(estado_inicial)
busca_profundidade(estado_inicial)



