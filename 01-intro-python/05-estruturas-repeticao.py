#for
palavra = 'Python'
for letra in palavra:
    print(letra)

numeros=[1, 2, 3, 4]
for numero in numeros:
    print(numero)


#range gera sequência numérica 
# range
# range (stop)
# range(5)= 0, 1, 2, 3, 4

# range (start, stop)
# range (4, 10)= 4, 5, 6, 7, 8, 9

# range (start, stop, stop)
# range (3, 10, 2)= 3, 5, 7, 9

for i in range(10):
    print (i)
    #funciona, mas não fazer isso^^^   
    #fazer isso\/
for numero in numeros:
    print (numeros)


# while

contador= 0
while contador < 5:
    print (contador)
    contador +=1
    # += é mais flexível que o ++, porque pode se alterar a qntd



#break
#pula o looping
# encontrar o primeiro número paar
numeros=[1, 3, 3, 4, 6]
for numero in numeros:
    if numero %2 == 0:
        print (numero)
break

#continue
#pula a interação
for numero in numeros:
    if numero <= 0:
        continue
    print (numero)

#sem continue
for numero in numeros:
    if numero > 0:
       print(numero)

#compreensão de listas
numeros=[2, 3, 4]
quadrados=[]

for numero in numeros:
    quadrados append(numero **2)

# é a mesma coisa^^^
quadrados= [numero ** 2 for numero in numeros]

numeros=[1, 4, 5, 4, 6]
pares=[]

for numero in numeros:
    if numero %2 = 0:
        pares append(numero)

# é a mesma coisa^^^
pares=[numero for numero in numeros if numero % 2 == 0]

# usar if no começo devolve numero, no fim devolve booleanos

# deixando as palavras em caps lock
palavras=['ola', 'mundo', 'teste']
palavra2=[palavra upper() for palavra in palavras ]