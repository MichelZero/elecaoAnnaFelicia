#
# autores:
# Anna Felícia Vasques Bezerra,
# Emilly Lopes,
# João Lucas Ferreira Pinheiro,
# Veluma  de Sousa Guedes e
# Suelyane Ferreira de Souza

from prettytable import PrettyTable
class Eleicao(PrettyTable):
  eleitores = list()
  candidatos = list()
  total = list()
  
  def __init__(self, eleitores, candidatos):
    self.eleitores = eleitores
    self.candidatos = candidatos
    self.tabelaEleitos = PrettyTable()  
    self.tabelaEleitor = PrettyTable()
    self.soma = 0
    
  def contaVotos(self):
    self.tabelaEleitos.field_names = ['VOTO', 'QUANTIDADE']
    for k in range(len(self.candidatos)):
      self.total.append([])
      self.soma = 0
      for i in range(len(self.eleitores) - 1):  
        if self.candidatos[k].numero == self.eleitores[i + 1].numero:
          self.soma += 1
      self.tabelaEleitos.add_row([self.candidatos[k].numero, self.soma])     
    return self.tabelaEleitos
  def contaEleitor(self):
    self.tabelaEleitor.field_names = ['CANDIDATO', 'NÚMERO', 'PARTIDO', 'CPF',]    
    for y in range(len(self.eleitores) - 1):
      self.tabelaEleitor.add_row([self.eleitores[y + 1].candidato, self.eleitores[y + 1].numero, self.eleitores[y + 1].partido, self.eleitores[y + 1].cpf])
    return self.tabelaEleitor         