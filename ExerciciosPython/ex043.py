# Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade mórbida

print('=-' * 7 + ' Calculo de IMC ' + '-=' * 7)

peso = float(input('|CALCULO DE IMC| Informe o seu peso: '))
altura = float(input('|CALCULO DE IMC| Informe sua altura: '))
imc = (peso/(altura*altura))

if imc < 18.5:
    print('IMC: {:.2f} | Abaixo do IMC.'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('IMC: {:.2f} | Peso Ideal'.format(imc))
elif imc >= 25 and imc < 30:
    print('IMC: {:.2f} | SOBREPESO'.format(imc))
elif imc >= 30 and imc < 40:
    print('IMC: {:.2f} | OBESIDADE'.format(imc))
else:
    print('IMC: {:.2f} | OBESIDADE MÓRBIDA'.format(imc))

print('=-' * 7 + ' Calculo de IMC ' + '-=' * 7)
