# Refaça o Desafio 009, mostrando a tabuada de um número
# que o usuário escolher, só que agora utilizando um laço for.

print('=-' * 5 + ' Tabuada v2.0 ' + '-=' * 5)

num_tab = int(input('|Tabuada v2.0| Digite: '))

for cont in range(0, 11):
    print('|\t   {} x {} = {}\t         |'.format(num_tab, cont, (num_tab*cont)))    

print('=-' * 5 + ' Tabuada v2.0 ' + '-=' * 5)
