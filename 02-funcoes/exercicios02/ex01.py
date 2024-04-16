#Ex01 - Jogo de Adivinhação: Peça ao usuário para adivinhar um número entre 1 e 100 que o programa escolheu aleatoriamente. Informe ao usuário se o palpite está alto ou baixo, até que ele acerte o número.

import random
def jogo_de_adivinhacao():
 numero_aleatorio = random.randint(1, 100)
 num=int(input('Digite um número entre 1 e 100 '))
 while numero_aleatorio != num:
  if numero_aleatorio == num:
    print('Número correto')
  elif numero_aleatorio > num:
    num=int(input('O palpite está baixo '))
  else:
    num=int(input('O palpite está alto '))
 print('Número correto')

jogo_de_adivinhacao()
