# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapaasar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada KM acima do limite.

print('= ' * 5 + ' RADAR City Limeira ' + ' =' * 5)

velo_car = int(input('VELOCIDADE DO CARRO: '))

if (velo_car > 80):
    velo_up = (velo_car - 80)
    val_mult = (velo_up * 7)
    print('Você está {} acima da Velocidade é foi Multado!!!'.format(velo_up))
    print('Valor multa: R${:.2f}'.format(val_mult))
else:
    print('Você está dentro do permitido da via! Limite: 80Km')
print('= ' * 5 + ' RADAR City Limeira ' + ' =' * 5)



