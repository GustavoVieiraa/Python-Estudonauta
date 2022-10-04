#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre
#quantos dólares ela pode comprar, considere o dolar US$1,00 = R$3,27

print('=' * 10 + 'Conversor de dolar' + '=' * 10)

v_real = float(input('Valor em reais: '))
v_dol = (v_real/3.27)
print('Você pode comprar US${:.2f} dollinhos.'.format(v_dol))
print('=' * 10 + 'Conversor de dolar' + '=' * 10)
