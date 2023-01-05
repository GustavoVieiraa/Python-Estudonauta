# Desenvolva um programa que leia o NOME, IDADE e SEXO de 4 pessoas.
# No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

print("=-" * 7 + " Analisador de dados " + "-=" * 7)
idade_old = 0
m_menor = 0
m = 0
for c in range(1, 5):
    nome = str(input('|Dados cliente: {} | Informe o seu nome: '.format(c)))
    idade = int(input('|Dados cliente: {} | Informe a sua idade: '.format(c)))
    sexo = str(input('|Dados cliente: {} | Informe o seu sexo: [M] ou [F]  '.format(c))).upper().strip()
    c += c
    m += idade
    if idade > idade_old and sexo == 'M':
        idade_old = idade
        nome_old = nome
    elif idade < 20 and sexo == "F":
        m_menor += 1
md = (m/4)
print("""
Dados clientes: {} média do GRUPO!
Dados clientes: {} é o homem mais velho do grupo com {} anos.
Dados clientes: {} têm menos de 20 anos.
""".format(md, nome_old, idade_old, m_menor))
print("=-" * 7 + " Analisador de dados " + "-=" * 7)
