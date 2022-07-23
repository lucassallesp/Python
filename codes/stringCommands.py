# Manipulando Texto.
from typing import List, Tuple

frase = 'Ola Mundo!'
frase2 = '   Aprenda Python  '
print(frase[0:5:2])  # [x:y:z] para fatiamento de uma string a partir da posição x até a posição z fatiadas de z em z.
print('Ola' in frase)  # in verifica se a string escolhida pertence à variável.
print(len(frase2))  # len() para analisar o numero de caracteres de uma string.
print(frase.find('Mundo', 0, 10))  # .find para mostrar a posição de onde está o caracter escolhido.
print(frase.count('o', 0, 10))  # .count para contar quantas vezes um caracter aparece na string.
print(frase.replace('Ola', 'Eai'))  # .replace para trocar um caracter por outro na string.
print(frase.upper())  # .upper para colocar toda string em maiúsculo.
print(frase.lower())  # .lower para colocar toda string em minúsculo.
print(frase.capitalize())  # .capitalize para colocar somente a primeira letra da string em maiúsculo.
print(frase.title())  # .title para colocar em maiúsculo a primeira letra de todas as palavras na string.
print(frase2.strip())  # .strip para remover espaços no inicio e no final da string.
print(frase2.rstrip())  # .rstrip para remover espaços pela direita.
print(frase2.lstrip())  # .lstrip para remover espaços pela esquerda.
print(frase.split())  # .split para fazer uma divisão na string. Split transforma uma string em listas diferentes.a: tuple[str, list[str]] = frase2.strip(), frase2.split()
print('-'.join(frase))


