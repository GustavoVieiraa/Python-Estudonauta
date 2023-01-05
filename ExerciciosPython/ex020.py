# O mesmo professor do desafio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que
# leia o nome dos quatro e mostre a ordem sorteada.

import random

print(' = ' * 5 + 'Sorteio de Pessoas' + ' = ' * 5)

a1 = str(input('Primeiro nome: '))
a2 = str(input('Segundo nome: '))
a3 = str(input('Terceiro nome: '))
a4 = str(input('Quatro nome: '))

lista_nomes = [a1, a2, a3, a4]
random.shuffle(lista_nomes)

print('A ordem de apresentação será:')
print(lista_nomes)


print(' = ' * 5 + 'Sorteio de Pessoas' + ' = ' * 5)
