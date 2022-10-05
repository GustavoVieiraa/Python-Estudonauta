# Crie um programa que leia um número Real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
#ex. Digite um número: 6.127, O número 6.127 tem a parte inteira 6.

# Na biblioteca Math podemos utilizar o Floor para pegar apenas a parte
#inteira de um número REAL.

from math import floor

print('=' * 5 + 'Valor INTEIRO' + '=' * 5)
num = float(input('Digite um número real: '))
print("{:=^20}".format(floor(num)))
print('=' * 5 + 'Valor INTEIRO' + '=' * 5)