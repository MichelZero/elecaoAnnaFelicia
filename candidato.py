#
# autores:
# Anna Felícia Vasques Bezerra,
# Emilly Lopes,
# João Lucas Ferreira Pinheiro,
# Veluma  de Sousa Guedes e
# Suelyane Ferreira de Souza

class Candidato:
  nome = None
  partido = None
  numero = None

  def __init__(self, nome, partido, numero):
    self.nome = nome
    self.partido = partido
    self.numero = numero