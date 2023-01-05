# Faça um programa que leia um ângulo qualquer e mostre na tela o valor
# do seno, cosseno e tangente desse ângulo.

from math import cos, radians, sin, tan, floor

print('=' * 10 + ' SENO, COSSENO e TANGENTE ' + '=' * 10)

a = float(input('Digite o ângulo desejado: '))

print('O ângulo de {} tem o SENO de {:.2f}'.format(a, sin(radians(a))))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(a, cos(radians(a))))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(a, tan(radians(a))))


print('=' * 10 + ' SENO, COSSENO e TANGENTE ' + '=' * 10)


