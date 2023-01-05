# Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores "M" ou "F". Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

from time import sleep


print('=-' * 7 + ' Validação de Genero em Python ' + '-=' * 7)

s = ''
masc = 0
fem = 0

while s != 'M' and s != 'F':
    s = str(input('|VALIDAÇÃO| Informe o seu sexo:  [M] ou [F] ')).upper()
    if s != 'M' and s != 'F':
        print('Você informou um valor errado, tente novamente')
        sleep(1)

print('O sexo escolhido foi {}.'.format(s))

print('=-' * 7 + ' Validação de Genero em Python ' + '-=' * 7)
