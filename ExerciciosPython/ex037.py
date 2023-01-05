# Escreva um programa que leia um número inteiro qualquer
# e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal

from time import sleep


print('=-' * 8 + ' Conversão de bases ' + '-=' * 8)

num_int = int(input('Digite um número inteiro: '))

base_esc = int(input("""
|CONVERSOR| Digite [1] para binário.
|CONVERSOR| Digite [2] para octal.
|CONVERSOR| Digite [3] para hexadecimal
Informe: """))
print('=-' * 8 + ' Convertendo... ' + '-=' * 8)
sleep(3)

if base_esc == 1:
    print('Número {} em binário é: {}'.format(num_int, str(bin(num_int)[2:])))
elif base_esc == 2:
    print('Número {} em octal é: {}'.format(num_int, str(oct(num_int)[2:])))
elif base_esc == 3:
    print('Número {} em hexadecimal é: {}'.format(num_int, str(hex(num_int)[2:])))
else:
    print('Opção invalida, tente novamente!')

print('=-' * 8 + ' Conversão de bases ' + '-=' * 8)