#Faça um programa que leia um número inteiro e mostre o seu sucessor e seu antecessor.

print('=-=' * 10)
num = int(input('Informe um número: '))
print('O antecessor de {} é {}.'.format(num, (num-1)))
print('O sucessor de {} é {}.'.format(num, (num+1)))
print('=-=' * 10)
