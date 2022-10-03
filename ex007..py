# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('=' * 30)
n1 = int(input('Informe a primeira nota: '))
n2 = int(input('Informe a segunda nota: '))
med = (n1+n2)/2
print('A média entre a primeira nota {} e a segunda nota {} é {}'.format(n1, n2, med))
print('=' * 30)