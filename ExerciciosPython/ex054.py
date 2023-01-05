# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade
# e quantas jão são de maior.

from datetime import date

print('=-' * 6 + ' Maioridade ' + '-=' * 6)

maior_i = 0
menor_i = 0

for n in range(1, 8):
    ano_nasc = int(input('|ANO DE NASCIMENTO| Informe seu ano de nascimento: '))
    ano_atual = date.today().year
    idade = (ano_atual-(ano_nasc))
    if idade > 18:
        maior_i += 1 
    else:
        menor_i += 1

print("""
Em seu sistema há:
    {} MAIORES DE IDADE
    {} MENORES DE IDADE
""".format(maior_i, menor_i))