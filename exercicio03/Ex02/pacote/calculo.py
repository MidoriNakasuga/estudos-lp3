def calcular_IMC(peso, alt):
    return (peso / (alt * alt))

def calcular_peso_ideal(alt):
    return (24.9 * (alt*alt))

def calcular_peso_perder(peso, peso_ideal):
    return (peso - peso_ideal)

def calcular_peso_ganhar(peso, peso_ideal):
    return (peso_ideal - peso)


