# pacote/main.py
import sys
import os

# Adiciona o diretório pai ao sys.path para permitir a importação do pacote aquario
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from pacote.calculos import calcular_volume, calcular_potencia_termostato, calcular_filtragem

if __name__ == "__main__":
    comprimento = float(input("Digite o comprimento do aquário em cm: "))
    altura = float(input("Digite a altura do aquário em cm: "))
    largura = float(input("Digite a largura do aquário em cm: "))
    temperatura_desejada = float(input("Digite a temperatura desejada em °C: "))
    temperatura_ambiente = float(input("Digite a temperatura ambiente em °C: "))

    volume = calcular_volume(comprimento, altura, largura)
    potencia = calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente)
    filtragem_min, filtragem_max = calcular_filtragem(volume)

    print(f"Volume do aquário: {volume:.2f} litros")
    print(f"Potência do termostato: {potencia:.2f} W")
    print(f"Filtragem necessária: entre {filtragem_min:.2f} e {filtragem_max:.2f} litros por hora")
