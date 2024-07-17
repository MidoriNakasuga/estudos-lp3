import sys
import os

# Adiciona o diretório pai ao sys.path para permitir a importação do pacote aquario
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pacote.calculo import calcular_IMC, calcular_peso_ideal, calcular_peso_final


if __name__ == "__main__":
    peso= float(input('Digite seu peso: '))
    alt= float(input('Digite sua altura: '))
    IMC = calcular_IMC(peso, alt)
    if IMC == 24.9:
       print('Classificação: Peso normal') 
    elif IMC != 24.9:
        peso_ideal = calcular_peso_ideal(alt)
        pesofinal= calcular_peso_final(peso - peso_ideal)

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

