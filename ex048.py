# Faça um programa que calcule a soma entre todos os números impares que são múltiplos
# de três e que se encontram no intervalo de 1 até 500.

from time import sleep


print('=-' * 5 + ' Impares ' + '-=' * 5)

for verificador in range(0, 500):
    if (verificador%3) == 0:
        s_de_multiplos = 0
        s_de_multiplos = (s_de_multiplos+verificador)

sleep(5)

print('O valor das somas dos números múltiplos de três de 1 a 500 é\t{}'.format(s_de_multiplos))

