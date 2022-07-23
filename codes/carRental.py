#Esse programa calcula quanto a pagar pelo aluguel de um carro.

dist = float(input('\nInforme a quantidade de Km percorridos com o carro: '))
dias = int(input('Informe por quantos dias o carro foi alugado: '))
preço = (60 * dias) + (0.15 * dist)
print(f'\nO preço a ser pago em {dias} dias de aluguel e {dist:.2f}km rodados é de R${preço:.2f}')
