# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar
# que tipo de triângulo será formado:
# - Equilátero: Todos os lados iguais
# - Isósceles: Dois lados iguais
# - Escaleno: Todos os lados diferentes

print('=-' * 7 + ' Qual triângulo irá formar? ' + '-=' * 7)

r1 = float(input('Digite o primeiro lado: '))
r2 = float(input('Digite o segundo lado: '))
r3 = float(input('Digite o terceiro lado: '))

if r1 == r2 and r2 == r3 and r1 == r3:
    print('Esse triangulo é EQUILÁTERO, pois tem todos os lados iguais!')
elif r1 != r3 and r3 == r2 and r3 == r1 or r1 != r2 and r2 == r3 and r3 == r1:
    print('Esse triângulo é ISÓSCELES, pois há dois lados iguais!')
else:
    print('Esse triângulo é ESCALENO, pois tem todos os lados diferentes!')
