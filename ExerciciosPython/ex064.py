# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição,
# de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando a flag).

### by gusta x:ii ###

print("-" * 5 + " Somador de Números v1.0 " + "-" * 5)

valEntrada = 0
quantNumsRecebidos = 0
somadorNumsRecebidos = 0
    ## Inicio Algoritmo
print("|Flag para parar| 999 ")
while valEntrada != 999:
    valEntrada = int(input("Digite um valor: "))
    if valEntrada != 999:
        quantNumsRecebidos += 1
        somadorNumsRecebidos += valEntrada
print("Valores Recebidos: {} | Valores Somados: {}".format(quantNumsRecebidos, somadorNumsRecebidos))
