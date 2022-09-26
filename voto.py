class Voto:
  cpf = None
  numero = None
  candidatos = list()
  eleitores = list()
  voto1 = False
  
  def __init__(self, cpf, numero, candidato, candidatos, eleitores):
    self.cpf = cpf
    self.numero = numero
    self.candidatos = candidatos
    self.eleitores = eleitores
    self.candidato = candidato
    self.partido = ''

  def votos(self):
    for v in range(len(self.eleitores)):
      if self.cpf == self.eleitores[v].cpf:
        voto1 = True 
        print('VOTO NÃO CONTABILIZADO. Este cpf já votou!')
        break
      else:
        voto1 = False
    if voto1 == False:
      for p in range(len(self.candidatos) - 1):
        if self.numero == self.candidatos[p + 1].numero:
          self.candidato = self.candidatos[p + 1].nome
          self.partido = self.candidatos[p + 1].partido
          voto1 = True
          print('VOTO CONTABILIZADO')
          return 'voto'
      self.partido = 'NULO'
      self.numero = 'NULO'
      self.candidato = 'NULO' 
      print('VOTO CONTABLILIZADO')    
      return 'nulo'