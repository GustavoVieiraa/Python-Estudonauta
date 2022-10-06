# Crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "SANTO"

print('=' * 8 + ' Sua cidade começa com SANTO? ' + '=' * 8)

nome_city = str(input('Qual nome da sua cidade: '))
nome_city = nome_city.upper()
nome_city = nome_city.split()
nome_city = nome_city[0]
print('Sua cidade começa com SANTO: {}'.format('SANTO' in nome_city))




print('=' * 8 + ' Sua cidade começa com SANTO? ' + '=' * 8)