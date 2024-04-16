#Ex03 - Contador de Vogais e Consoantes: Peça ao usuário para digitar uma frase e retorne o número de vogais e consoantes na frase.
def contador():
 frase=input('Digite uma frase: ')
 vog='aiueoáéíóúãõàèìùòâêîôû' #todos as opções para garantir
 con=sum(letra.isalpha() and letra not in vog for letra in frase)#fução isalpha() foi sugerida na pesquisa
 num_vog=sum(letra in vog for letra in frase)
 print(f'O número de vogais é: {num_vog}. E o número de consoantes é: {con}')

contador()