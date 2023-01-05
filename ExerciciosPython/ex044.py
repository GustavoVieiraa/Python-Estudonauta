# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:
# À Vista dinheiro/cheque: 10% de desconto
# À Vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

print('------ Produto comprado ------')
val_produto = float(input('|VALOR PRODUTO| R$'))
print('''
=----------OPÇÕES DE PAGAMENTO----------=
à vista dinheiro/cheque - opção[0]
à vista no cartão - opcão [1]
Até 2x no cartão - opção [2]
3x ou mais no cartão - opção [3]
=---------------------------------------=
''')
opc_pag = int(input('OPÇÃO DE PAGAMENTO: '))


if opc_pag == 0:
    desc = ((val_produto*10)/100)
    print("""
    Valor Produto: R${:.2f}
    Valor Desconto: R${:.2f}
    Valor do Produto com o Desconto: R${:.2f}
    Forma de Pagamento: à vista dinheiro/cheque [10% de desconto]
    """.format(val_produto, desc, (val_produto-desc)))
elif opc_pag == 1:
    desc = ((val_produto*5)/100)
    print("""
    Valor Produto: R${:.2f}
    Valor Desconto: R${:.2f}
    Valor do Produto com o Desconto: R${:.2f}
    Forma de Pagamento: à vista no cartão [5% de desconto]
    """.format(val_produto, desc, (val_produto-desc)))
elif opc_pag == 2:
    print("""
    Valor Produto: R${:.2f}
    Dividido em 2x de R${:.2f}
    Forma de Pagamento: 2x no cartão [sem desconto]
    """.format(val_produto, (val_produto/2)))
elif opc_pag == 3:
    juros = ((val_produto*20)/100)
    qt_pag = int(input('|QUANTAS VEZES| '))
    print("""
    Valor Produto: R${:.2f}
    Valor Juros: R${:.2f}
    Valor do Produto com o Juros: R${:.2f}
    Froma de Pagamento: {}x de R${:.2f} no cartão [20% de juros]
    """.format(val_produto, juros, (val_produto+juros), qt_pag, ((val_produto+juros)/qt_pag)))
else:
    print('Opção invalida, tente novamente!')