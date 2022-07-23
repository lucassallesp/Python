#Esse programa sorteia alguém para apagar um quadro numa turma de 4 pessoas.

from random import choice
a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
a4 = str(input('Digite o nome do quarto aluno: '))
lista = [a1, a2, a3, a4]
s = choice(lista)
print(f'O aluno sorteado para apagar o quadro foi: {s}!!!')
