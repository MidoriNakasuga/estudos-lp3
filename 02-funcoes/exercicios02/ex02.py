#Ex02 - Tabuada de Um Número: Solicite ao usuário um número e exiba a tabuada desse número de 1 a 10.
def tabuada():
 num=int(input('Digite um número '))
 tab=1
 while tab != 11:
  res= tab*num
  print(f'{num} x {tab} = {res}')
  tab=tab+1

tabuada()
