# Crie um programa que faça o computador jogar Jokenpô com você.

import random

print('=-' * 7 + ' Pedra, Papel, Tesoura... ' + '-=' * 7)

lista_game = ["Pedra".upper(), "Papel".upper(), "Tesoura".upper()]
esc_computador = random.choice(lista_game)

esc_jogador = int(input("""
|JOKENPÔ|  Pedra  - opção[ 0 ]
|JOKENPÔ|  Papel  - opção[ 1 ]
|JOKENPÔ| Tesoura - opção[ 2 ]
opção: """))

if esc_jogador == 0:
    esc_jogador = 'Pedra'.upper()
elif esc_jogador == 1:
    esc_jogador = 'Papel'.upper()
elif esc_jogador == 2:
    esc_jogador = 'Tesoura'.upper()

if esc_computador == 'PEDRA' and esc_jogador == 'TESOURA' or esc_computador == 'TESOURA' and esc_jogador == 'PAPEL' or esc_computador == 'PAPEL' and esc_jogador == 'PEDRA':
    print("""
    |=====================|
    |    Escolha PC - {}  |
    |  Escolha Player - {}|
    |  Computador WIN!!!  |
    |=====================|
    """.format(esc_computador.capitalize(), esc_jogador.capitalize()))
elif esc_jogador == 'PEDRA' and esc_computador == 'TESOURA' or esc_jogador == 'TESOURA' and esc_computador == 'PAPEL' or esc_jogador == 'PAPEL' and esc_computador == 'PEDRA':
    print("""
    |=====================|
    |    Escolha PC - {}  |
    |  Escolha Player - {}|
    |    Player WIN!!!    |
    |=====================|
    """.format(esc_computador.upper(), esc_jogador.upper()))
else:
    print("""
    |=====================|
    |    Escolha PC - {}  |
    |  Escolha Player - {}|
    |     empate!!!       |
    |=====================|
    """.format(esc_computador.upper(), esc_jogador.upper()))