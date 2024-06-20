#Ex01. Crie um programa que recebe como entrada o comprimento, altura e a largura de um aquário e calcule 
#as seguintes informações.

    #O volume do aquário em litros;
    #A potência do termostato necessária para manter a temperatura adequada dentro do aquário;
    #A quantidade em litros de filtragem por hora necessária para manter a qualidade da água.

    #Volume é dado por (comprimento * altura * largura) / 1000
    #A potência do termostato depende do tamanho do aquário e da temperatura ambiente. 
#Para o cálculo utilizar a fórmula: potencia = volume * 0,05 * (temperatura desejada - temperatura ambiente)
    #A quantidade de filtragem por hora deve ser no mínimo 2 a 3 vezes o volume do aquário.
def ex1():
    temp_amb=30
    temp_des=27
    comp= float(input('Digite o comprimento'))
    alt= float(input('Digite a altura'))
    larg= float(input('Digite a largura'))
    vol = (comp * alt * larg)/1000
    pot = vol * 0.05 * (temp_des - temp_amb)
    fil = 2 * vol
    filt = 3 * vol
    print(f'O volume é: {vol}. A potência necessária do termostato é: {pot}. A quantidade de filtragem por hora deve ser no mínimo de {fil} a {filt}')

ex1()