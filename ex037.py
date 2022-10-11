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

if num_int%2 == 1 or num_int%2 == 0:
    binario_list = [].append(num_int%2)
    num_int = num_int // 2
    print(binario_list)
