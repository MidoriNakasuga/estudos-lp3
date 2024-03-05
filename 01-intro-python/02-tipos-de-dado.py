# tipos de daods
# int, float, string, list, tuple, set
# dict
# none

# int
idade = 18
temperatura = -2

# flot
altura = 1.61
PI = 3.14

# string
nome = "Sasadabina"
nome = 'Sasadabina'
# funciona como um array, pode acessar as letras individuais a partir de []
print (nome[0])
print (nome [-1])
print (nome[0:3])
# nome é um objeto da classe str
# nome tem o que? metodos
print (nome.capitalize())
print (nome)

# char?
# n tem TT
letra = 'a'
letra = 'A'

# interpolação de str e variáveis
nome = 'passaralho'
tempo = 23
mensagem = f'Olá {nome}. Você tem {tempo} anos'
print (mensagem)

# list
# lista de valores
# pode ser alterada
habilidades = []
habilidades = ['java', 'css', 'html', 'c#', 'sql']
print(habilidades[1])
habilidades[0] = 'ruby'
habilidades.append('javascript') 
habilidades.insert(0,'php')
print(habilidades)

# tuple
# "lista" de valores que não pode alterar
habilidades = ['java', 'css', 'python'] # list
opcoes = ('sim', 'não', 'talvez') # tuple

# for
for opcao in opcoes:
    print(opcao)

for habilidade in habilidades:
    print(habilidade)

# set
# não indexado
# não permite elementos duplicados
# digite a mensagem
# digite os emails de destino
# sabina@gmail.com
# sabinada@gmail.com
# sabina@gmail.com
emails = {'sabina@gmail.com', 'sabinada@gmail.com', 'sabinada@gmail.com'}
emails.add('sabinada@gmail.com')
print (emails)


# dict
# dicionario
# chave : valor
# key : value

# site de emprego
empresa = 'Google'
titulo = 'Engenheiro de software'
salario = 20000.00
remoto = False

# vaga
vaga = {
    'empresa' : 'Google',
    'titulo' : 'Engenheiro de software',
    'salario' : 20000.00,
    'remoto' : False
}

print (vaga['salario']) # mostra o valor a partir da chave

# None
nome = None

