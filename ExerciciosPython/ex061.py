# Refaça o Desafio 51, lendo o primeiro termo e a razão
# de uma PA, mostrando os 10 primeiros termos da progressão
# usando a estrutura while.

print('=-' * 5 + ' Progressão Aritmética v2.0 ' + '-=' * 5)

a = int(input('|Primeiro Termo| digite: '))
r = int(input('|Razão| digite: '))
c = 0
while c < 10:
    print(a, end=' → ')
    a += r
    c += 1

print('Fim'+'\n'+'=-' * 5 + ' Progressão Aritmética v2.0 ' + '-=' * 5)
