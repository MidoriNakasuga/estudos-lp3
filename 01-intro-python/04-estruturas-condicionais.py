#if
# if condição:
#    codigo
#    codigo
# codigo >>>> fora do if

idade = 20
if idade >= 18:
    print('Maioridade')

#if/else
if idade >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')

#if/eliif/else
# criança 0 a 12
# adolescente de 13 a 17
# adulto d18 a 59
# idoso 60+

if idade > 0 and idade <= 12:
    print('Criança')
if idade > 12 and idade <= 17:
    print('Adolescente')
if idade > 17 and idade <= 59:
    print('Adulto')
if idade > 59:
    print('Idoso')
#>>>>> testa todos

if idade <= 12:
    print('Criança')
elif idade <= 17:
    print('Adolescente')
elif idade <= 59:
    print('Adulto')
else:
    print('idoso')
#>>>>>> para quando da certo


# condiçoes aninhadas
email = 'admin@gmail.com'
senha = '123'

if email == 'admin@gmail.com':
    if senha == '123':
        print('liberado')
    else: 
        print('erro')
else:
    print('erro')

if email == 'admin@gmail.com' and senha == '123':
    print('liberado')
else:
    print('erro')
    
# entrada email, senha
# saida True ou false

def liberar_acesso(email,senha):
    if email == 'admin@gmail.com' and senha == '123':
        return True
    else:
        return False

def liberar_acesso(email,senha):
    return email == 'admin@gmail.com' and senha == '123'


# dia 1, 2, 3, 4, 5, 6, 7
# palavra domingo, segunda, terça, quarta, quinta, sexta, sábado

dia = 3

lista = ['domingo','segunda', 'terca']
dia=dia-1
print(lista[dia])

dias = {
    1: domigo,
    2: segunda,
    3: terca,
    4: quarta,
    5: quinta,
    6: sexta,
    7: sabado
}

if dia in dias:
    print (dias[dia])

for chave in dias.keys():
    print(chave)

#operador ternário

idade = 12,0
#status pode ser maior ou menor
#status=?

if idade >= 18:
    status='maior'
else:
    status='menor'
  #utilizando o operador
status = 'maior' if idade >= 18 else 'menor'    

#match
  #é o switch do python
dia = 3

match dia:
        case 1:
             print('Domingo')
        case 2:
            print('Segunda')
        case 3:
            print('Terça')
        case 4:
            print('Quarta')
        case 5:
            print('Quinta')
        case 6:
            print('Sexta')
        case 7:
            print('Sábado')
        case _:
            print('Inválido')

match dia:
    case 1 | 7:
        print('Fim de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia de semana')



