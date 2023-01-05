#Escreva um programa que pergunte a quantidade de KM percorridos
# por um carro alugado e a quantidade de dias pelos quais ele
# foi alugado. Calcule o preço a pagar, sabendo que o carro custa,
# R$60,00 por dia e R$0,15 por KM rodado.

print('=' * 12 + ' concessionária Gusta ' + '=' * 12)

car_alu = str(input('Carro alugado: '))
pag_day = int(input('Quantos dias você ficou com o/a {}: '.format(car_alu)))
pag_km = int(input('Quantos KMs você andou com o/a {} nesses {} dias: '.format(car_alu, pag_day)))

val_dias = (pag_day*60)
val_kms = (pag_km*0.15)

print('Você ficou {} dias com o/a {} e andou {}KMs.'.format(pag_day, car_alu, pag_km))
print('Total a pagar por dias {}: R${:.2f}  [R$60 por dia]'.format(pag_day, val_dias))
print('Total a pagar por KMs {}: R${:.2f} [R$0,15 por KM rodado]'.format(pag_km, val_kms))
print('Total a pagar: R${:.2f}'.format(val_dias+val_kms))


print('=' * 12 + ' concessionária Gusta ' + '=' * 12)

