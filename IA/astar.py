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

		self.grid[self.um[1]-1][self.um[0]-1] = 1
		self.grid[self.dois[1]-1][self.dois[0]-1] = 2
		self.grid[self.tres[1]-1][self.tres[0]-1] = 3
		self.grid[self.quatro[1]-1][self.quatro[0]-1] = 4
		self.grid[self.cinco[1]-1][self.cinco[0]-1] = 5
		self.grid[self.seis[1]-1][self.seis[0]-1] = 6
		self.grid[self.sete[1]-1][self.sete[0]-1] = 7
		self.grid[self.oito[1]-1][self.oito[0]-1] = 8

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






tabuleiro = tabuleiro()
tabuleiro.embaralha()
tabuleiro.printa_tabuleiro()
print tabuleiro.procura_vazio()
