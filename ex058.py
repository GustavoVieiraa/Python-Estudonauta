# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
# em um número entre 0 e 10. Só que agora o jogador vai tentar
# adivinhar até acertar, mostrando no final quantos palpites foram
# necessários para vencer.

import random

print('=-' * 7 + ' Random Game v2.0 ' + '-=' * 7)

esc_pc = random.randint(0, 10)
esc_player = -1
t = 0
while esc_pc != esc_player:
    esc_player = int(input('|PLAYER| Digite um valor: '))
    if esc_pc == esc_player:
        t += 1
        print('Parabéns, você acertou com {} tentativas!'.format(t))
    if esc_pc != esc_player:
        t += 1
        print('Tente novamente...')
print('=-' * 7 + ' Random Game v2.0 ' + '-=' * 7)
