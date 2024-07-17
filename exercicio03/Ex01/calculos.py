# pacote/calculos.py

def calcular_volume(comprimento, altura, largura):
    return (comprimento * altura * largura) / 1000

def calcular_potencia_termostato(volume, temperatura_desejada, temperatura_ambiente):
    return volume * 0.05 * (temperatura_desejada - temperatura_ambiente)

def calcular_filtragem(volume):
    return volume * 2, volume * 3
