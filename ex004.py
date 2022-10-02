 #Mais alguns tipos primitivos através do dissecamento de uma Variável

alg = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é {} e possui {} caracteres'.format(type(alg), len(alg)))
print('Só tem espaços? ', alg.isspace())
print('É alfabetico? ', alg.isalpha())
print('É um número? ', alg.isnumeric())
print('Está escrito em MAIUSCULO? ', alg.isupper())
print('Está escrito somente em MINUSCULO? ', alg.islower())
print('Está capitalizada? ', alg.istitle())
