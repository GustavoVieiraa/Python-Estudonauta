#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

from math import hypot

print('=' * 10 + ' Calculando Hipotenusa ' + '=' * 10)

cat_oposto = float(input('Comprimento do cateto oposto: '))
cat_adjacente = float(input('Comprimento do cateto adjacente: '))
h = hypot(cat_oposto, cat_adjacente)

print('A hipotenusa tera como resultado: {:.2f}'.format(h))
