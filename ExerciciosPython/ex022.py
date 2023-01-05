# Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiúsculas
# -> O nome com todas as letras minúsculas
# -> Quantas letras ao todo (sem considerar espaços)
# -> Quantas letras tem o primeiro nome

print('= ' * 5 + 'Informações nome' + ' =' * 5)
name = str(input('Qual é seu nome: ')).strip()

espaces = name.count(' ')
qnt_name = len(name)
nome_lista = name.split()

print('Nome com todas as letras maisculas: {}'.format(name.upper()))
print('Nome com todas as letras minusculas: {}'.format(name.lower()))
print('Seu nome tem {} letras ao todo (sem considerar espaços)'.format(qnt_name-espaces))
print('Seu primeiro nome é {}, e tem {} letras.'.format(nome_lista[0], len(nome_lista[0])))

print('= ' * 5 + 'Informações nome' + ' =' * 5)

