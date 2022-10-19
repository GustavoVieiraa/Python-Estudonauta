# Faça um programa que leia um número qualquer e mostre
# o seu fatorial. ex: 5! = 5x4x3x2x1.

from math import factorial


print('=-' * 5 + ' Fatorial ' + '-=' * 5)

n_fat = int(input('|INFORME UM NÚMERO| '))
resultado = factorial(n_fat)
while n_fat > 0:
    if n_fat == 1:
        print('{}'.format(n_fat), end='')
    else:
        print("{}x".format(n_fat), end='')
    n_fat -= 1
print(end='' + ' = ' + '{}'.format(resultado)) 
print('\n' + '=-' * 5 + ' Fatorial ' + '-=' * 5)
