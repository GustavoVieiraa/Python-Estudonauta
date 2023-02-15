# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999,
# que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre eles (desconsidere o flag).

## by gusta x:ii ##

print("=-=" * 5 + " Somador de Valores " + "=-=" * 5)

# variaveis
numDigitados = 0
somaNums = 0

print("|=--- FLAG PARA SAIR [999] ---=|")

while True:
    valEntrada = int(input("Digite um valor: "))
    if valEntrada == 999:
        break
    else:
        numDigitados += 1
        somaNums += valEntrada

print("=-=" * 3 + " DADOS SOFTWARE " + "=-=" * 3)
print("O total de números digitados foi: {}".format(numDigitados))
print("A soma entre todos os números digitados foi: {}".format(somaNums))
print("=-=" * 3 + " DADOS SOFTWARE " + "=-=" * 3)
