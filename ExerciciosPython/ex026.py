# Faça um programa que leia uma frase pelo teclado e informe:
# -> Quantas vezes aparece a letra 'A'
# -> Em que posição ela aparece a primeira vez.
# -> Em que posição ela aparece a ultima vez.

print('-' * 10 + ' Verificando Letras ' + '-' * 10)

frase = str(input('Digite uma frase: ')).strip()
print('A letra A aparece {}x na frase ({}).'.format(frase.upper().count('A'), frase))
print('A letra A aparece primeiro na posição {}'.format(frase.upper().find('A')+1))
print('A letra A aparece pela ultima vez na posição {}'.format(frase.upper().rfind('A')+1))


print('-' * 10 + ' Verificando Letras ' + '-' * 10)
