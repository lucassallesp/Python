#Esse programa lê um ângulo qualquer e mostra na tela o valor do seno cosseno e tangente desse ângulo.

import math
ang = int(input('Digite o valor de um ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))
print(f'O seno de {ang}° é: {sen:.2f} \nO cosseno de {ang}° é: {cos:.2f} \nA tangente de {ang}° é: {tg:.    2f}')