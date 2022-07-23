#Esse programa lê o comprimento do cateto oposto e adjacente de um triangulo e mostra a sua hipotenusa.

import math
op = float(input('Digite o comprimento do cateto oposto do triângulo: '))
adj = float(input('Digite o comprimento do cateto adjacente do triângulo: '))
hip = math.sqrt(op**2 + adj**2)
print(f'A hipotenusa desse triângulo vale: {hip}')



