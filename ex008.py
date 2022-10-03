# Escreva um programa que leia um valor em metros e o exiba convertido 
# em centimetros e milímetros.

print('=' * 10 + 'Conversor de medidas' + '=' * 10)

val_m = float(input('valor em metros: '))
val_cm = val_m * 100
val_mm = val_cm * 10
print('O valor em metros é {}'.format(val_m))
print('O valor em centimetros é {}'.format(val_cm))
print('O valor em milimetros é {}'.format(val_mm))

print('=' * 10 + 'Conversor de medidas' + '=' * 10)
