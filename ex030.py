# Crie um programa que leia um número inteiro e mostre na tela se ele é
# PAR ou IMPAR

print('= ' * 10 + ' Par ou Impar ' + ' =' * 10)

num = int(input('Digite um número: '))
if ((num%2) == 0):
    print('Esse número {} é PAR'.format(num))
else:
    print('Esse número {} é IMPAR!'.format(num))

print('= ' * 10 + ' Par ou Impar ' + ' =' * 10)

