# Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.

print('=-' * 6 + ' Verificador de Pesos ' + '-=' * 6)

for v in range(1, 7):
    peso = float(input('|PESO| Informe seu peso (Kg): '))
    if v == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if maior_peso < peso:
            maior_peso = peso 
        elif menor_peso > peso:
            menor_peso = peso

print("""
O MAIOR peso informado foi {:.1f}Kg
O MENOR peso informado foi {:.1f}Kg
""".format(maior_peso, menor_peso))
print('=-' * 6 + ' Verificador de Pesos ' + '-=' * 6)

