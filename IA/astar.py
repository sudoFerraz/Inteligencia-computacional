from random import seed
from random import randrange
import numpy
from random import choice
import random

class tabuleiro():
	def __init__(self):
		self.um = [4,4]
		self.dois = [4,4]
		self.tres = [4,4]
		self.quatro = [4,4]
		self.cinco = [4,4]
		self.seis = [4,4]
		self.sete = [4,4]
		self.oito = [4,4]
		self.grid = [[0, 0, 0],[0, 0, 0],[0, 0, 0]]
		self.pecas = [self.um, self.dois, self.tres, self.quatro, self.cinco,\
		self.seis, self.sete, self.oito]
		self.custo = 0


	def atualiza_pecas(self):
		self.pecas = [self.um, self.dois, self.tres, self.quatro, self.cinco,\
		self.seis, self.sete, self.oito]

		self.grid[self.um[1]-1][self.um[0]-1] = 1
		self.grid[self.dois[1]-1][self.dois[0]-1] = 2
		self.grid[self.tres[1]-1][self.tres[0]-1] = 3
		self.grid[self.quatro[1]-1][self.quatro[0]-1] = 4
		self.grid[self.cinco[1]-1][self.cinco[0]-1] = 5
		self.grid[self.seis[1]-1][self.seis[0]-1] = 6
		self.grid[self.sete[1]-1][self.sete[0]-1] = 7
		self.grid[self.oito[1]-1][self.oito[0]-1] = 8


	def atualiza_com_vazio(self, vazio_novo):
		self.pecas = [self.um, self.dois, self.tres, self.quatro, self.cinco,\
		self.seis, self.sete, self.oito]

		self.grid[self.um[1]-1][self.um[0]-1] = 1
		self.grid[self.dois[1]-1][self.dois[0]-1] = 2
		self.grid[self.tres[1]-1][self.tres[0]-1] = 3
		self.grid[self.quatro[1]-1][self.quatro[0]-1] = 4
		self.grid[self.cinco[1]-1][self.cinco[0]-1] = 5
		self.grid[self.seis[1]-1][self.seis[0]-1] = 6
		self.grid[self.sete[1]-1][self.sete[0]-1] = 7
		self.grid[self.oito[1]-1][self.oito[0]-1] = 8

		self.grid[vazio_novo[1]][vazio_novo[0]] = 0
		

	def verifica_unico(self, posicao):
		if posicao == self.um:
			return False
		elif posicao == self.dois:
			return False
		elif posicao == self.tres:
			return False
		elif posicao == self.quatro:
			return False
		elif posicao == self.cinco:
			return False
		elif posicao == self.seis:
			return False
		elif posicao == self.sete:
			return False
		elif posicao == self.oito:
			return False
		else:
			return True

	def posicao_aleatoria(self):
		coluna = numpy.random.choice(numpy.arange(1,4), p=[0.33, 0.33, 0.34])
		linha = numpy.random.choice(numpy.arange(1,4), p=[0.33, 0.33, 0.34])
		posicao = [coluna, linha]
		return posicao


	def embaralha(self):
		while self.um == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.um = posicao

		while self.dois == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.dois = posicao

		while self.tres == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.tres = posicao

		while self.quatro == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.quatro = posicao

		while self.cinco == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.cinco = posicao

		while self.seis == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.seis = posicao

		while self.sete == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.sete = posicao

		while self.oito == [4,4]:
			posicao = self.posicao_aleatoria()
			if self.verifica_unico(posicao):
				self.oito = posicao

		self.atualiza_pecas()

	def printa_tabuleiro(self):
		for linha in self.grid:
			print linha

	def procura_vazio(self):
		linha = 0
		coluna = 0
		posicao_vazio = []
		for linha_ in self.grid:
			linha = linha + 1
			coluna = 0
			for coluna_ in linha_:
				coluna = coluna + 1
				if coluna_ == 0:
					posicao_vazio.append(coluna)
					posicao_vazio.append(linha)
					return posicao_vazio

	def possiveis_movimentos(self):
		peca_vazia = self.procura_vazio()
		movimentos_possiveis = []
		for peca in self.pecas:
			if peca[0] == peca_vazia[0]:
				if peca[1] == peca_vazia[1] + 1 or peca[1] == peca_vazia[1] -1:
					movimentos_possiveis.append(peca)
			elif peca[1] == peca_vazia[1]:
				if peca[0] == peca_vazia[0] + 1 or peca[0] == peca_vazia[0] -1:
					movimentos_possiveis.append(peca)
		return movimentos_possiveis


	def gera_filhos(self):

		peca_vazia = self.procura_vazio()
		movimentos = self.possiveis_movimentos()
		filhos = []
		vazio_novo = []

		for movimento in movimentos:
			new_tabuleiro = tabuleiro()
			if movimento == self.um:
				new_tabuleiro.um = peca_vazia
				vazio_novo = self.um
			else:
				new_tabuleiro.um = self.um

			if movimento == self.dois:
				new_tabuleiro.dois = peca_vazia
				vazio_novo = self.dois
			else:
				new_tabuleiro.dois = self.dois

			if movimento == self.tres:
				new_tabuleiro.tres = peca_vazia
				vazio_novo = self.tres
			else:
				new_tabuleiro.tres = self.tres

			if movimento == self.quatro:
				new_tabuleiro.quatro = peca_vazia
				vazio_novo = self.quatro
			else:
				new_tabuleiro.quatro = self.quatro

			if movimento == self.cinco:
				new_tabuleiro.cinco = peca_vazia
				vazio_novo = self.cinco
			else:
				new_tabuleiro.cinco = self.cinco

			if movimento == self.seis:
				new_tabuleiro.seis = peca_vazia
				vazio_novo = self.seis
			else:
				new_tabuleiro.seis = self.seis

			if movimento == self.sete:
				new_tabuleiro.sete = peca_vazia
				vazio_novo = self.sete
			else:
				new_tabuleiro.sete = self.sete

			if movimento == self.oito:
				new_tabuleiro.oito = peca_vazia
				vazio_novo = self.oito
			else:
				new_tabuleiro.oito = self.oito

			


			new_tabuleiro.atualiza_pecas()
			new_tabuleiro.custo = self.custo + 1
			filhos.append(new_tabuleiro)

		return filhos





	def calcula_h1(self):
		soma = 0
		aux = 0
		if self.um != [1, 1]:
			aux = aux + self.um[0] - 1
			aux = aux + self.um[1] - 1
			soma = soma + aux
			aux = 0
		if self.dois != [2, 1]:
			aux = aux + abs(self.dois[0] - 2)
			aux = aux + self.dois[1] -1
			soma = soma + aux
			aux = 0
		if self.tres != [3, 1]:
			aux = aux + abs(self.tres[0] - 3)
			aux = aux + self.tres[1] - 1
			soma = soma + aux
			aux = 0
		if self.quatro != [3, 2]:
			aux = aux + abs(self.quatro[0] - 3)
			aux = aux + abs(self.quatro[1] - 2)
			soma = soma + aux
			aux = 0
		if self.cinco != [3, 3]:
			aux = aux + abs(self.cinco[0] - 3)
			aux = aux + abs(self.cinco[1] - 3)
			soma = soma + aux
			aux = 0
		if self.seis != [2, 3]:
			aux = aux + abs(self.seis[0] - 2)
			aux = aux + abs(self.seis[1] - 3)
			soma = soma + aux
			aux = 0
		if self.sete != [1, 3]:
			aux = aux + self.sete[0] - 1
			aux = aux + abs(self.sete[1] - 3)
			soma = soma + aux
			aux = 0
		if self.oito != [1, 2]:
			aux = aux + self.oito[0] - 1
			aux = aux + abs(self.oito[1] - 2)
			soma = soma + aux
			aux = 0
		return soma 

	def calcula_h2(self):
		soma = 0
		if self.um != [1, 1]:
			soma = soma + 1
		if self.dois != [2, 1]:
			soma = soma + 1
		if self.tres != [3, 1]:
			soma = soma + 1
		if self.quatro != [3, 2]:
			soma = soma + 1
		if self.cinco != [3, 3]:
			soma = soma + 1
		if self.seis != [2, 3]:
			soma = soma + 1
		if self.sete != [1, 3]:
			soma = soma + 1
		if self.oito != [1, 2]:
			soma = soma + 1
		return soma



tabuleiro_init = tabuleiro()
tabuleiro_init.embaralha()
tabuleiro_init.printa_tabuleiro()
print tabuleiro_init.procura_vazio()
tabuleiro_init.possiveis_movimentos()
print tabuleiro_init.calcula_h1()
print tabuleiro_init.calcula_h2()
filhos = tabuleiro_init.gera_filhos()
for filho in filhos:
	print "\n"
	filho.printa_tabuleiro()








