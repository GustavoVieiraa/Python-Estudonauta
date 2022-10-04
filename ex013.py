#Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário, com 15% de aumento.

print('=' * 15 + ' Aumento de 15% Jr para Pl ' + '=' * 15)

v_sal = float(input('Informe o seu salário: R$'))
v_aum = ((v_sal*15)/100)

print('Seu salário atual é R${:.2f}'.format(v_sal))
print('Você teve um aumento de R${:.2f}, é referente a 15%'.format(v_aum))
print('Salário novo: R${:.2f}'.format(v_sal+v_aum))


print('=' * 15 + ' Aumento de 15% Jr para Pl ' + '=' * 15)