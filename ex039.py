# Faça um software que leia o ano de nascimento de um jovem
# e informe, de acordo com a sua idade: 
# - Se ele ainda vai se alistar ao serviço militar
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deve mostrar o tempo que passou ou o que falta.

from datetime import date
from time import sleep

print('=-' * 8 + ' Alistamento Militar ' + '-=' * 8)

ano_nasc = int(input('|EXERCITO BRASILEIRO| Ano Nascimento: '))
ano_atual = date.today().year
idade = (ano_atual-ano_nasc)

print('=-' * 8 + ' Verificando... ' + '-=' * 8)
sleep(2)

if idade <= 17:
    print('|EXERCITO BRASILEIRO| Você tem {} anos, ainda faltam {} anos para você se alistar!'
    .format(idade, (18-idade)))

elif idade == 18:
    print('|EXERCITO BRASILEIRO| Você tem {} anos, você tem a idade exata para se apresentar!'
    .format(idade))

elif idade > 18:
    print('|EXERCITO BRASILEIRO| Você tem {} anos, passou {} anos do alistamento!'
    .format(idade, (idade-18)))

print('=-' * 8 + ' Alistamento Militar ' + '-=' * 8)
