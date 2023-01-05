# Faça um programa que mostre na tela uma contagem regressiva 
# para o estouro de fogos de artifício, indo de 10 até 0,
# com pausa de 1 segundo entre eles.

from time import sleep

print('=-' * 5 + ' contagem regressiva ' + '-=' * 5)

for contagem in range(10, -1, -1):
    print("CONTAGEM: {}".format(contagem))
    sleep(1)
print('=-' * 5 + ' Feliz ano novo!!! ' + '-=' * 5) 