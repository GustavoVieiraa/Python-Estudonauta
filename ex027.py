# Faça um programa que leia o nome completo de uma pessoa, mostrando
# em seguida o primeiro e o último nome separadamente.

print('= ' * 8 + 'Primeiro e ultimo nome' + ' =' * 8)

nome = str(input('informe o seu nome: '))
nome = nome.split()
ult_nome = len(nome)-1
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[ult_nome]))

print('= ' * 8 + 'Primeiro e ultimo nome' + ' =' * 8)
