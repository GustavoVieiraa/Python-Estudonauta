# Faça um programa que mostre a tabuada de vários números,
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado
# for negativo.

## by gusta x:ii ##

contTabuada = True

# Para finalizar a tabuada, basta digitar um número NEGATIVO.

while contTabuada == True:
    print('=-=' * 3 + ' Tabuada 100% atualizada ' + '=-=' * 3)
    numTabuada = int(input("Escolha uma Tabuada: "))
    if numTabuada < 0:
        break
    else: 
        for c in range (11):
            print("{} x {} = {}".format(numTabuada, c, (numTabuada*c)))
