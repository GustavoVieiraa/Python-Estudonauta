# Faça um programa que leia três números e mostre qual é o 
# maior e o menor número.

print('-' * 10 + ' Verificador de números ' + '-' * 10)

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
n3 = int(input('Digite mais um valor: '))

if n1 > n2 and n1 > n3:
    print('O maior valor digitado foi: {}'.format(n1))
    if n2 > n3:
        print('O menor número digitado foi: {}'.format(n3))
    else:
        print('O menor número digitado foi: {}'.format(n2))
elif n2 > n1 and n2 > n3:
    print('O maior número digitado foi: {}'.format(n2))
    if n1 > n3:
        print('O menor número digitado foi: {}'.format(n3))
    else:
        print('O menor número digitado foi: {}'.format(n1))
elif n3 > n1 and n3 > n2:
    print('O maior número digitado foi: {}'.format(n3))
    if n1 > n2:
        print('O menor número digitado foi: {}'.format(n2))
    else:
        print('O menor número digitado foi: {}'.format(n1))
        
print('-' * 10 + ' Verificador de números ' + '-' * 10)
