# Faça um programa que leia um número inteiro e diga
# se ele é ou não um número primo.

print('=-' * 5 + ' Número Primo? ' + '-=' * 5)

num = int(input('|VERIFICAÇÃO| Digite um número inteiro: '))

tot = 0

for cont in range(1, num + 1):
    if num % cont == 0:
        tot += 1
print('O número {} foi divisivel por {} vezes'.format(num, tot))
if tot == 2:
    print('E por isso o número {} é um número PRIMO!'.format(num))
else:
    print('E por isso o número {} não é um número primo!'.format(num))