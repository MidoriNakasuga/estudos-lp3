# Função
print("ola")
sum([1, 3, 5])  

# quero somar uma lista de números
# -->usar a função sum

# quero calcular a média de notas dos alunos ---> fazer as seguintes perguntas
# 1. tem no python?
# 2. alguém já programou? (copia ou adiciona dependencia)
# 3. (se todos são não) -->declarar 

# 1. Declaração
# def nome_funcao(paramentro1, PARAMETRO2)
# return valor
# 

# 2. Chamada
print("ola")
sum([1, 3, 5])  
# nome_funcao('dad', 1)

# função sem retorno e sem parâmentros
def imprimir_mensagem():
    print('Socorrooooo')

imprimir_mensagem()
imprimir_mensagem()


# Função sem retorno e com parâmentros
# parametros vs argumentos
def saudacoes(nome):
    print(f'Bom dia {nome}')

# argumento para o parâmemtro nome Sabinada
saudacoes('Sabinada')

# argumento para o parâmemtro nome
nome_completo= 'Samuel Chen'
saudacoes(nome_completo)

# Função com retorno e sem parâmentros
def obter_mensagens():
    return 'socorro'

mensagem = obter_mensagens()
print(mensagem)

print(obter_mensagens)

# Função com retorno e com parâmentros 
def gerar_saudacao(nome):
    return f'Bom dia {nome}'

print(gerar_saudacao('Pedrão'))
print(gerar_saudacao('Malana'))

#  retornos   parâmetros
#    não         não
#    não         sim
#    sim         não
#    sim         sim     (adequado) (funcao pura)

# imprimir saudacao
# saudacao = frase(dinamica) nome (dinamico)
# 'Bom dia Kokada'
# 'Boa tarde Saboga'
# 'Noiite mori'

def saudacao(nome, frase):
    print(f'{frase} {nome}')

def saudacao(nome, frase):
    return f'{frase} {nome}'

print(saudacao ('Fada', 'Bodiaa'))
print(saudacao (nome = 'Fada', frase = 'Bodiaa'))
print(saudacao (frase = 'Bodiaa', nome = 'Fada'))
print(saudacao ('Fada', frase = 'Bodiaa' ))

# parametro ocm valor padrao 
def saudacao(nome, frase = "Bom dia"):
   return f'{frase} {nome}'



# Entrada

notas_alunos = [ [1.0, 2.0, 3.0], 
                 [4.0, 5.0, 6.0], 
                 [7.0, 8.0, 9.0]]


# Saida [2.0, 5.0, 8.0]
def calcular_medias(notas):
    return sum(notas)/ len(notas)

def calcular_media_alunos(notas_alunos):
   # medias = []
    
   # for notas in notas_alunos:
   #  media = calcular_medias(notas)
   #  medias.append(media)
   #  return medias

 #medias = calcular_media_alunos
  return [calcular_medias(notas) for notas in notas_alunos]

# numero = 6
# numeros = [6, 4, 5]
# notas_alunos= [ [1, 10, 3], [10, 4, 0]]
# for valor in numeros:
#   print(valor)
# for valor in notas_alunos

def imprimir_medias(notas_alunos):
 medias = calcular_media_alunos(notas_alunos)
 print (medias)
# logica de enviar medias por email


