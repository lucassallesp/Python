#Esse programa lê o nome completo de uma pessoa e mostra algumas especificações.

nome: str = (input('Digite o seu nome completo: '))
n = (nome.split()[0])
m = (nome.replace(' ', ''))
print(f'O seu nome em letras maiúsculas é: {nome.upper()}\n'
      f'O seu nome em letras minúsculas é: {nome.lower()}\n'
      f'O seu nome possui {len(m)} letras ao todo!\n'
      f'O seu primeiro nome tem {len(nome.split()[0])} letras!')
print(nome.title())
print(nome.capitalize())
print('.'.join(nome.split()))

