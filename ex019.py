# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

print('=' * 10 + ' Quem vai apagar??? ' + '=' * 10)

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))

lista_nomes = [a1, a2, a3, a4]

print('O aluno que vai apagar o quadro será: ', random.choice(lista_nomes))

print('=' * 30)