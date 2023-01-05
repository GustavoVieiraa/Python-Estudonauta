# Escreva um programa que faça o computador "pensar" em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador. O programa deverá escrever na tela se o usuário
# venceu ou perdeu.

import random
import time

print('-' * 10 + ' Random Game ' + '-' * 10)

num_computer = random.randint(0, 5)
num_player = int(input('informe um número: '))
if (num_computer == num_player):
    time.sleep(3)
    print('Parabéns, você acertou o número!')
    print('Sua escolha: {}'.format(num_player))
    print('Escolha PC: {}'.format(num_computer))
else:
    time.sleep(3)
    print('Você errou! tente novamente!')
    print('Sua escolha: {}'.format(num_player))
    print('Escolha PC: {}'.format(num_computer))

print('-' * 10 + ' Random Game ' + '-' * 10)
