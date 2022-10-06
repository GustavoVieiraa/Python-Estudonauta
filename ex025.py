# Crie um programa que leia o nome de uma pessoa e diga se
# ela tem "SILVA" no nome.

print('-' * 8 + ' Você é Silva? ' + '-' * 8)

name = str(input('Como você se chama? '))
name = name.upper()
print('O seu nome tem SILVA? {}'.format('SILVA' in name))


print('-' * 8 + ' Você é Silva? ' + '-' * 8)
