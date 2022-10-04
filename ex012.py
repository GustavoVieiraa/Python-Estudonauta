#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, 
# com 5% de desconto.

print('=' * 15 + ' Promoção de 5% ' + '=' * 15)

v_prod = float(input('Informe o valor do produto: R$'))
v_prod_desc = ((v_prod*5)/100)

print('Valor do Produto: R${:.2f}'.format(v_prod))
print('Valor do desconto: R${:.2f}'.format(v_prod_desc))
print('Valor do Produto com o desconto de 5%: R${:.2f}'.format(v_prod-v_prod_desc))

print('=' * 15 + ' Promoção de 5% ' + '=' * 15)