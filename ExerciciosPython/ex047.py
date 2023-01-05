#  Crie um programa que mostre na tela todos os números
# pares que estão no intervalo entre 1 e 50.

print("=-" * 5 + ' Números pares de 1 até 50! ' + '-=' * 5)

print('CONJUNTO DE PARES [0, 50]: ', end='')
for cont in range(0, 52, 2):
    print("{} ".format(cont), end='')

print('\n' + "=-" * 5 + ' Números pares de 1 até 50! ' + '-=' * 5)
