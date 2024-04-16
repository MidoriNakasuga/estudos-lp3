#Ex05 - Verificador de Palíndromos: Solicite ao usuário que digite uma palavra ou frase e verifique se é um palíndromo (ou seja, pode ser lida de frente para trás e de trás para frente da mesma forma).
def palindromo():
    texto = input("Digite uma palavra ou frase: ")
    texto 
    texto = texto.replace(" ", "")
    if texto == texto[::-1]: 
        print('É um palíndromo')
    else:
        print('Não é um palíndromo')

palindromo()