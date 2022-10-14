# Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão.

print('=-' * 5 + ' Progressão aritmética ' + 5 * '-=')

a = int(input('|PRIMEIRO TERMO| Informe: '))
r = int(input('|RAZÃO PA| Informe: ' ))

for c in range(a, ((r*10)+a), r):
    print(c)

print('=-' * 5 + ' Progressão aritmética ' + 5 * '-=')
