#Ex06 - Conversor de Notas Escolares: Baseado em uma pontuação fornecida pelo usuário (0 a 100), converta para o sistema de notas A, B, C, D, ou F, seguindo os padrões de conversão comuns.
def conversor():
    nota=int(input('Insira sua nota de 0 a 100'))
    if nota >= 90:
        print('Nota A')
    elif nota >= 80:
        print('Nota B')
    elif nota >= 70:
        print('Nota C')
    elif nota >= 60:
        print('Nota D')
    else:
        print('Nota F')
#A: 90-100
#B: 80-89
#C: 70-79
#D: 60-69
#F: abaixo de 60
conversor()