# Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. O programa deve 
# perguntar ao usuário se ele quer ou não continuar a digitar valores.

## by gusta x:ii ##

print("=-=" * 4 + " Verificador de Valores v.001 " + "=-=" * 4)


    # declaração variaveis
continuarVerificacao = True
somValores = 0
quantEntradaNums = 0

while continuarVerificacao == True:
    valNum = int(input("Informe Valor: "))
    if quantEntradaNums == 0:
        maiorNum = valNum
        menorNum = valNum
    else:
        if valNum > maiorNum:
            maiorNum = valNum
        if valNum < menorNum:
            menorNum = valNum
    somValores += valNum
    quantEntradaNums += 1
    querCont = str(input("Continuar [S/N]: ")).upper().strip()
    if querCont == "N":
        continuarVerificacao = False
    else:
        while querCont != 'S' and querCont != 'N':
            querCont = str(input("Continuar [S/N]: ")).upper().strip()
            if querCont == 'N':
                continuarVerificacao = False
print("=----------- Dados Tratados -----------=")
print("Soma dos Valores: {}".format(somValores))
print("Média dos Valores: {}".format(somValores/quantEntradaNums))
print("Valores recebidos: {}".format(quantEntradaNums))
print("Maior Valor: {} | Menor Valor: {}".format(maiorNum, menorNum))
print("=----------- Dados Tratados -----------=")