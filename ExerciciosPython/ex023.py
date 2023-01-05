# Faça um programa que leia um número de 0 a 9999 e mostre
# na tela cada um dos dígitos separados.

print('-' * 8 + ' Unidades, dezenas, centenas e milhares ' + '-' * 8)

num = int(input('Digite um valor: '))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print(' Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print(' Milhar: {}'.format(m))

print('-' * 8 + ' Unidades, dezenas, centenas e milhares ' + '-' * 8)
