# Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5.0: REPROVADO
# - Média entre 5.0 e 6.9: RECUPERAÇÃO
# - Média 7.0 ou superior: APROVADO

from time import sleep

print('=-' * 8 + ' Escola Leovegildo Chagas Santos ' + '-=' * 8)

n1_aluno = float(input('|ESCOLA ESTADUAL| Digite a 1º nota: '))
n2_aluno = float(input('|ESCOLA ESTADUAL| Digite a 2º nota: '))

m_aluno = ((n1_aluno+n2_aluno)/2)

print('=-' * 8 + ' Calculando média & resultado ' + '-=' * 8)
sleep(3)

if m_aluno < 5:
    print('Sua média foi {}, você foi REPROVADO!'.format(m_aluno))
elif m_aluno >= 5 and m_aluno <= 6.9:
    print('Sua média foi {}, você ficou de RECUPERAÇÃO'.format(m_aluno)) 
else:
    print('Sua média foi {}, você foi APROVADO!'.format(m_aluno))

print('=-' * 8 + ' Escola Leovegildo Chagas Santos ' + '-=' * 8)
