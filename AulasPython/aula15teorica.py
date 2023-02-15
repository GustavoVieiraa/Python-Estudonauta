# Aula 15 - Interrompendo repetições While

# Vamos utilizar o Looping infinito While True, e quando encontrar-mos
# a informação, dado, ou o que procuramos, vamos finalizar através do Break.

# Parte Pratíca:

c = 1
while c <= 10:
    print(c, '... ', end='')
    c += 1
    if c > 7:
        break
print("Fim...")