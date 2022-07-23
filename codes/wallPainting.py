#Esse programa calcula a quantidade necessária de tinta para se pintar uma parede a partir de suas medidas.
#Cada litro de tinta pinta uma área de 2m².

largura = float(input('\nInforme a largura da parede: '))
altura = float(input('Informe a altura da parede: '))
area = largura * altura
tinta = area / 2.0
print(f'\nA sua parede tem as dimensões de {largura} x {altura} e sua área é de {area}m²')
print(f'A quantidade de tinta necessária para pintar essa parede é de {tinta} litros')



