#Ex08 - Função de Contagem de Palavras: Escreva uma função que receba uma string (frase) como argumento e retorne um dicionário onde as chaves são as palavras únicas no texto e os valores são o número de vezes que cada palavra aparece no texto. Depois, teste a função com diferentes textos fornecidos pelo usuário.
def cont_palavra(frase):
    palavras = frase.split()
    frequencia = dict()
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1
    return frequencia
frase = input('Digite uma frase')
print(cont_palavra(frase))
