#Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário, com 15% de aumento.

print('=' * 15 + ' Aumento de 15% Jr para Pl ' + '=' * 15)

v_sal = float(input('Informe o seu salário: '))
v_aum = ((v_sal*15)/100)

print('Seu salário atual é R${}'.format(v_sal))
print('Você teve um aumento de R${}, é referente a 15%'.format(v_aum))
print('Salário novo: R${}'.format(v_sal+v_aum))


print('=' * 15 + ' Aumento de 15% Jr para Pl ' + '=' * 15)