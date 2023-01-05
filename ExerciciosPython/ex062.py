# Melhore o DESAFIO 61, perguntando para o usuário
# se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que
# quer mostrar 0 termos.

print('=-' * 5 + ' Progressão Aritmética v3.0 ' + '-=' * 5)

c = 0
cont = 0
val_c = 0
esc = 'S'
p_term = int(input('|Primeiro termo| Digite: '))
r = int(input('|Razão| Digite: '))
while c < 10:
    esc = ''
    print(p_term, end=' → ')
    p_term += r
    c += 1
esc = (input('|Continuar?| [S/N] : blu')).upper()
while(esc == 'S'):
    if (esc == 'S'):
        c = 0
        rep = (int(input('|Termos| Quantos termos a mais? Digite: ')))
        while c < rep:
            esc = ''
            print(p_term, end= ' → ')
            p_term += r
            c += 1
        esc = (input('|Continuar?| [S/N] : ')).upper()

print('Obrigado por utilizar o nosso Software!')
print('\n'+'=-' * 5 + ' Progressão Aritmética v2.0 ' + '-=' * 5)

