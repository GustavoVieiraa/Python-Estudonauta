#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('=--=' * 8)
number = int(input('Digite um valor: '))
num_dob = number * 2
num_tri = number * 3
num_raiz = number ** 2
print('O dobro de {} é igual {}.'.format(number, num_dob))
print('O triplo de {} é igual {}.'.format(number, num_tri))
print('A raiz quadrada de {} é igual {}.'.format(number, num_raiz))
print('=--=' * 8)
