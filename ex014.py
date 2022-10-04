#Escreva um programa que converta uma temperatura digitada em C° 
# e converta em F°

print('=' * 30)

temp_c = float(input('Temperatura em graus C°: '))
temp_f = ((9*temp_c)/5)+32
print('A temperatura de {} C° corresponde a {} F°.'.format(temp_c, temp_f))

