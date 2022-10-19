# Crie um programa que leia dois valores e mostre um MENU
# na tela:
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa
# seu programa deverá realizar a operação solicitada em cada caso.

print('=-' * 7 + ' Menu de opções ' + '-=' * 7)
nome = str(input('|NOME| informe seu nome: ')).strip()
n1 = int(input('|N1| Digite valor um: '))
n2 = int(input('|N2| Digite valor dois: '))
esc = 0
while esc != 5:
    er = 0
    esc = 0
    cont = ''
    print("""=------------------=
    {}, gostaria de selecionar qual opção?
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa\n=------------------=""".format(nome))
    while esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc != 5:
        esc = int(input('select: '))
        if esc != 1 and esc != 2 and esc != 3 and esc != 4 and esc != 5:
            print('Opção invalida, tente novamente!')
            er += 1
        if er > 3:
            print('Você não está prestando atenção, verifique as opções.')
    if esc == 1:
        print('A soma entre N1: {} e N2: {} é {}'.format(n1, n2, (n1+n2)))
        while cont != 'S' and cont != 'N': # Estrutura para validação do usuário se quer continuar ou não...
            cont = str(input('{}, gostaria de continuar? [S] ou [N] '.format(nome))).upper().strip()
            if cont != 'S' and cont != 'N':
                print('Opção invalida, tente novamente!')
            if cont == 'N':
                esc = 5
    elif esc == 2:
        print('A multiplicação entre N1: {} e N2: {} é {}'.format(n1, n2, (n1*n2)))
        while cont != 'S' and cont != 'N': # Estrutura para validação do usuário se quer continuar ou não...
            cont = str(input('{}, gostaria de continuar? [S] ou [N] '.format(nome))).upper().strip()
            if cont != 'S' and cont != 'N':
                print('Opção invalida, tente novamente!')
            if cont == 'N':
                esc = 5
    elif esc == 3:
        if n1 > n2:
            print('O N1: {} é > (maior) que o N2: {}'.format(n1, n2))
        else:
            print('O N2: {} é > (maior) que o N1: {}'.format(n2, n1))
        while cont != 'S' and cont != 'N': # Estrutura para validação do usuário se quer continuar ou não...
            cont = str(input('{}, gostaria de continuar? [S] ou [N] '.format(nome))).upper().strip()
            if cont != 'S' and cont != 'N':
                print('Opção invalida, tente novamente!')
            if cont == 'N':
                esc = 5
    elif esc == 4:
            n1 = int(input('|N1| Digite valor um: '))
            n2 = int(input('|N2| Digite valor dois: '))
print('{}, obrigado por utilizar nosso Menu de opções'.format(nome))
print('=-' * 7 + ' Menu de opções ' + '-=' * 7)
