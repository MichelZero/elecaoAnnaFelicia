#
# autores:
# Anna Felícia Vasques Bezerra,
# Emilly Lopes,
# João Lucas Ferreira Pinheiro,
# Veluma  de Sousa Guedes e
# Suelyane Ferreira de Souza


from candidato import Candidato as C
from prettytable import PrettyTable 
from voto import Voto as V
from eleicao import Eleicao as E

candidatos = list()
T0 = C('NULO', 'NULO', 'NULO')
candidatos.append(T0)
igual = False

total = list()

eleitores = list()
E0 = V(False, False, False, candidatos, eleitores)
eleitores.append(E0)
voto1 = False

tabela = PrettyTable()
tabela.field_names = ['CANDIDATO', 'PARTIDO', 'NÚMERO']

while True:
  print('\n+-------------------------------+'
  '\n|1 - ADCIONAR CANDIDATO         |'
  '\n|2 - LISTAR CANDIDATOS          |'
  '\n|3 - VOTAR                      |'
  '\n|4 - QUANTIDADE DE VOTOS        |'
  '\n|5 - ELEITORES                  |'
  '\n|6 - SAIR                       |'
  '\n+-------------------------------+')
  a = int(input('Digite sua opção:'))
  if a == 1:
    nome = input('Informe o nome do candidato: ')
    partido = input('Informe o partido: ')
    numero = str(input('Informe o numero:'))
    T1 = C(nome, partido.upper(), numero)
    for i in range(len(candidatos)):
      if candidatos[i].numero == T1.numero:
        igual = True
        break
      else:
        igual = False
    if igual == True:
      print(f'Já existe um candidato com o numero {T1.numero}')
    elif igual == False:
      candidatos.append(T1)
      tabela.add_row([T1.nome, T1.partido, T1.numero])
      print('CANDIDATO ADICIONADO')

  elif a == 2:
    print(f'{tabela}')

  elif a == 3:
    cpf = str(input('Informe seu cpf:'))
    numero2 = str(input('Informe o numero do candidato:'))
    E1 = V(cpf, numero2, False, candidatos, eleitores)
    l = E1.votos()
    if l == 'voto':
      eleitores.append(E1)
    elif l == 'nulo' :
      eleitores.append(E1)
    
  elif a == 4:
    M = E(eleitores, candidatos)
    print(f'{M.contaVotos()}')
    
  elif a == 5:
    M = E(eleitores, candidatos)
    print(f'{M.contaEleitor()}')    
      
  elif a == 6:
    break
    
  else:
    print('INFORME UM NÚMERO VÁLIDO')