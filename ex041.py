# A confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua categoria, de acordo
# com a sua idade.
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SENIOR
# Acima de 20 anos: MASTER

print('=-' * 7 + ' Confederação Nacional de Natação ' + '-=' * 7)

idade = int(input('|CONFEDERAÇÃO| Idade: '))

if idade > 0 and idade <= 9:
    print('|CONFEDERAÇÃO| Você é um atleta MIRIM!')
elif idade > 9 and idade <= 14:
    print('|CONFEDERAÇÃO| Você é um atleta INFANTIL!')
elif idade > 14 and idade <= 19:
    print('|CONFEDERAÇÃO| Você é um atleta JUNIOR!')
elif idade == 20:
    print('|CONFEDERAÇÃO| Você é um atleta SENIOR!')
elif idade > 20:
    print('|CONFEDERAÇÃO| Você é um atleta MASTER!')
else:
    print('Você informou um número invalido, tente novamente!')

print('=-' * 7 + ' Confederação Nacional de Natação ' + '-=' * 7)