# Desenvolva um programa que pergunte a distância de uma viagem
# em Km. Calcule o preço da passagem, cobrando R$0,50 por KM para viagens 
# até 200Km e R$0,45 para viagens mais longas.

print('= ' * 8 + ' CNC Viagens ' + ' =' * 8)

dist = int(input('Distância da Viagem: '))
if (dist <= 200):
    val_viagem = (dist*0.5)
    print('Sua viagem terá {}KMs e Custará R${:.2f}'.format(dist, val_viagem))
else:
    val_viagem = (dist*0.45)
    print('Sua viagem terá {}KMs e Custará R${:.2f}'.format(dist, val_viagem))
    
print('= ' * 8 + ' CNC Viagens ' + ' =' * 8)

