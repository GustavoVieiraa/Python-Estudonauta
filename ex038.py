# Escreva um programa que leia dois números inteiros e compare-os,
# mostrando na tela uma mensagem:
# * O primeiro valor é maior 
# * O segundo valor é maior
# * Não existe valor maior, os dois são iguais

from time import sleep


print('=-' * 8 + ' Verificador de valores ' + '-=' * 8)

n1 = int(input('Digite o 1º valor: '))
n2 = int(input('Digite o 2º valor: '))

print('=-' * 8 + ' Averiguando os valores... ' + '-=' * 8)
sleep(3)

if n1 > n2:
    print('O valor {} é maior que o valor {}'.format(n1, n2))
elif n2 > n1:
    print('O valor {} é maior que o valor {}'.format(n2, n1))
else:
    print('Não existe um valor maior, os dois valores são iguais!')
    
print('=-' * 8 + ' Verificador de valores ' + '-=' * 8)