# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor do seu aumento.
# Para salários superiores a R$1.200,00 calcule um aumento de 10%.
# Para os salários inferiores ou iguais, o aumento deve ser de 15%.

print('=-' * 7 + ' Aumento salarial ' + '-=' * 7)

sal_atual = float(input('Salário atual: '))
if sal_atual > 1200:
    aum_sal = (sal_atual*10)/100
    sal_atual = (sal_atual+aum_sal)
    print('Seu aumento foi de 10% - R${:.2f}, seu novo salário é R${:.2f}'.format(aum_sal, sal_atual))
elif sal_atual <= 1200:
    aum_sal = (sal_atual*15)/100
    sal_atual = (sal_atual+aum_sal)
    print('Seu aumento foi de 15% - R${:.2f}, seu novo salário é R${:.2f}'.format(aum_sal, sal_atual))
else:
    print('Valor invalido, verifique novamente!')
print('=-' * 7 + ' Aumento anual ' + '-=' * 7)
