# Escreva um programa para aprovar o empréstimo bancário para a
# compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o emprestimo será negado!

from time import sleep


print('=-' * 10 + ' MINHA CASA & MINHA VIDA ' + '-=' * 10)

val_casa = float(input('|CAIXA ECONOMICA| Valor da casa: R$'))
sal_comprador = float(input('|CAIXA ECONOMICA| Salário atual: R$'))
anos_pagamento = int(input('|CAIXA ECONOMICA| Quantos anos você pretende pagar: '))

limite_prestacao = ((sal_comprador*30)/100)
val_prestacao_casa = val_casa / (anos_pagamento*12)

print('=-' * 10 + ' Analisando dados no sistema... ' + '-=' * 10)
sleep(5)

if limite_prestacao < val_prestacao_casa:
    print('|CAIXA ECONOMICA| Infelizmente, o seu limite de crédito não foi aprovado.')
elif limite_prestacao > val_prestacao_casa:
    print("""|CAIXA ECONOMICA| Parabéns, seu crédito foi aprovado! 
|CAIXA ECONOMICA| Você ira pagar a casa em {}x
|CAIXA ECONOMICA| O seu limite era de R${:.2f}!
|CAIXA ECONOMICA| A prestação da sua casa ficou em R${:.2f}
""".format((anos_pagamento*12), limite_prestacao, val_prestacao_casa))

print('=-' * 10 + ' MINHA CASA & MINHA VIDA ' + '-=' * 10)
