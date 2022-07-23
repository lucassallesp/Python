#Esse programa mostra quantos dolares ela pode comprar com o dinheiro que possui.

n = float(input('Quantos reais você tem na carteira? '))
print('Cotação atual do dólar: R$3,27')
print(f'Você pode comprar: ${(n / 3.27):.2f} com R${n:.2f}!')