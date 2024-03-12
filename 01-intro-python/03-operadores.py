# operadores aritmeticos
# +, -, *, /, **
nota1=10.0
nota2=5.5
nota3=7.5
media=(nota1 + nota2 + nota3)/ 3

#numero elevado a outro
# e elevado a 2
# 10 elevado a 3
numero = 10
numero_elevado_2= numero * numero
nemero_elevado_3= numero * numero * numero

#operadores lógicos
# and, or, not
print(3+2)#5
print(True and True)#True
print(True and False)#False
print(False and True)#False
print(False and False)#False

print(True or True)#True
print(True or False)#True
print(False or True)#True
print(False or False)#False

print(not True)#False
print(not False)#True

#permitir entrada 
# - uuario for funcionario E
# - usuario não estiver bloqueado E
# - a hora atual estiver entre 8 e 18 horas 

#permitir entrada
# - adm

usuario_funcionario = True
usuario_bloqueado = False
hora_atual = 17
usuario_adm = False

horario_comercial = hora_atual >= 8 and hora_atual <= 18
funcionario_ativo = usuario_funcionario and not usuario_bloqueado

if usuario_adm or (funcionario_ativo and horario_comercial)
   print('acesso permitido')


idade = 22
maioridade = idade >= 18

if maioridade:
    pass


#operadores de comparaçao
# ==, !=, <, >, <=, >=
# == compara valores
# = atribui valores


idade = 24
maioridade = idade >= 18

if media >= 6.0:
    print('aprovado')

# is, is not >>> exclusivopython
#operador de identidade 
# comparar se os objetos ocupam o mesmo 
# espaço de memória

a = [1, 2, 3]
b = [1, 2, 3]
print(a==b) #True
print(a is b) #False

c = b

print (b is c)#True

# operador in, not in
# verificar se elemento existe ou não em uma sequência
# str, list, tuple
opcoes = ('sim', 'não', 'talvez')
opcao = input('digite uma opção')
opcao in opcoes
if opcao in opcoes:
    print('ok')
else:
    print('nao tem essa opcao')

opcao = opcao.lower()
opcap = opcao.srip()

numeros = [1, 3, 5, 6]
for numero in numeros:
    print ('numero')