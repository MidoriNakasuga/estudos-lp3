#crie um programa em Python que recebe como entada o valor de uma compra e apresenta como saída o valor final com desconto e o desconto aplicado com base nas seguintes regras;

# compras entre 0,01 e 9,99 - 0% de desconto
# compras entre 10,00 e 99,99 - 5% de desconto
# compras entre 100,00 e 499,99 - 10% de desconto
# compras iguais ou seperiores 500,00 - 15% de desconto

compra=float(input("Digite o valor da compra"))
if compra > 0.0 and compra <= 9.99:
             print(compra)
elif compra > 9.99 and compra <= 99.99:
        desconto=(compra/100) * 5
        valorfinal=(compra - desconto)
        print(f'O valor final é de:{valorfinal} e o desconto foi de: {desconto}')
elif compra > 99.99 and compra <= 499.99:
        desconto=(compra/100) * 10
        valorfinal=(compra - desconto)
        print(f'O valor final é de:{valorfinal} e o desconto foi de: {desconto}')
elif compra > 500.00:
        desconto=(compra/100) * 15
        valorfinal=(compra - desconto)
        print(f'O valor final é de:{valorfinal} e o desconto foi de: {desconto}')
else:
        print('Valor inválido')