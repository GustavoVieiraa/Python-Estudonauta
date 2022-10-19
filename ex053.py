# Crie um programa que leia uma frase qualquer e 
# diga se ela é um palíndromo, desconsiderando os espaços
# ex. apos a sopa
# ex. a sacada da casa
# ex. a torre da derrota

from time import sleep


print('=-' * 5 + ' Identificador de Palíndromo ' + '-=' * 5)

frase = str(input('Digite uma frase: ')).strip()
frase = frase.replace(' ', '')
lista_pali = []
for v in range(len(frase), 0, -1):

    lista_pali.append(frase[v-1])

pali = ''.join(lista_pali)

if pali == frase:
    print('A frase {} ao invertida é {}'.format(frase, pali))
    print('A frase {} é um Palíndromo!'.format(frase))
else:
    print('A frase {} invertida é {}'.format(frase, pali))
    print('A frase {} não é um Palíndromo.'.format(frase))