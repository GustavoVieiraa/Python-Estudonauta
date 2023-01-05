# Faça um programa que calcule a soma entre todos os números impares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

from time import sleep


print('=-' * 5 + ' Impares ' + '-=' * 5)
r = 0
c = 0
for verificador in range(1, 501, 2):
    if verificador%3 == 0:
        r += verificador
        c += 1
sleep(5)

print('Todos os {} números impares divisiveis por 3 somados resultam o valor de: {}'.format(c, r))