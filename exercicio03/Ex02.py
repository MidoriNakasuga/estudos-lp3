#Ex02. Utilizando as diretrizes de Índice de Massa Corporal (IMC) da Organização Mundial de Saúde (OMS), 
#crie uma calculadora que solicita ao usuário seu peso (Kg) e sua altura (m) e apresenta em qual classificação 
#o indivíduo se encaixa. Além disso, o programa deve apresentar quanto o indivíduo precisa perder ou ganhar de 
#peso para chegar no peso normal (imc = 24,9).

#IMC = peso / altura * altura

#Classificação
#----------------------------------
#IMC           Classificação
#-----------------------------------
#< 18,5             Baixo peso
#18,5 a 24,9     Peso normal
#25,0 a 29,9     Excesso de peso
#30,0 a 34,9     Obesidade de Classe 1
#35,0 a 39,9     Obesidade de Classe 2
#>= 40,00         Obesidade de Classe 3
def ex2():
    peso= float(input('Digite seu peso'))
    alt= float(input('Digite sua altura'))
    IMC = peso / (alt * alt)
    if IMC == 24.9:
        print('Classificação: Peso normal') 
    elif IMC != 24.9:
        peso_ideal = 24.9 * (alt * alt)
        pesofinal= peso - peso_ideal

    if IMC < 18.5:
        print(f'Classificação: Baixo peso. Precisa ganhar: {pesofinal}')
    elif IMC < 24.9:
        print(f'Classificação: Peso normal. Precisa ganhar: {pesofinal}')
    elif IMC < 29.9:
        print(f'Classificação: Excesso de peso. Precisa perder: {pesofinal}')
    elif IMC < 34.9:
        print(f'Classificação: Obesidade Classe 1. Precisa perder: {pesofinal}')
    elif IMC < 39.9:
        print(f'Classificação: Obesidade Classe 2. Precisa perder: {pesofinal}')
    elif IMC >= 40.0:
        print(f'Classificação: Obesidade Classe 3. Precisa perder: {pesofinal}')

ex2()