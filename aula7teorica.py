"""Como vimos na aula 7 - Operadores Aritméticos temos alguns operadores
que podemos utilizar na Linguagem Python para realizar operações.
Temos os operadores +, -, *, /, **, // e %. Cada um deles com as suas propriedades
e utilizam basicamente o mesmo seguimento que utilizamos em nosso dia a dia com
matemática, com apenas algumas diferenças.

Temos também a ordem de precedência deles, quem vem primeiro quando temos uma grande expressão?
1º - Primeiro damos prioridade para os parênteses (), 
2º - segundo lugar temos exponenciação **, 
3º - terceiro lugar temos uma galera *, /, //, %,
4º - quarto lugar temos os sinais + e - . """

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
exp = n1 ** n2
div = n1 / n2
divint = n1 // n2
restdiv = n1 % n2
print('='*70)
print('Resultado da soma dos valores {} e {} é {}.'.format(n1, n2, s))
print('Resultado da subtração dos valores {} e {} é {}.'.format(n1, n2, sub))
print('Resultado da exponenciação dos valores {} e {} é {}.'.format(n1, n2, exp))
print('Resultado da divisão dos valores {} e {} é {:.2f}'.format(n1, n2, div))
print('Resultado da divisão inteira dos valores {} e {} é {}'.format(n1, n2, divint))
print('='*70) 