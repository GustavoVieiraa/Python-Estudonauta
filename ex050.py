# Desenvolva um programa que leia seis números inteiros
# e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for impar, desconsidere-o.

print('=-' * 5 + ' Você é PAR? ' + '-=' * 5)

s = 0
lista_pares = []

for cont in range(0, 6):
    num = int(input('Digite um número: '))
    if (num%2) == 0:
        s = (s+num)
        lista_pares.append(num)    

print('Os números PARES digitados foram {} e a soma deles é {}.'.format(lista_pares, s))

print('=-' * 5 + ' Você é PAR? ' + '-=' * 5)
