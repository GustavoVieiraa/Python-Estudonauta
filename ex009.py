# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('=' * 30)
n_tab = int(input('Digite um valor: '))
print("""
Tabuada do número {}
{} x 1 = {}
{} x 2 = {}
{} x 3 = {}
{} x 4 = {}
{} x 5 = {}
{} x 6 = {}
{} x 7 = {}
{} x 8 = {}
{} x 9 = {}
{} x 10 = {}
""".format(n_tab, n_tab, (n_tab*1), n_tab, (n_tab*2), n_tab, (n_tab*3), n_tab, (n_tab*4),
 n_tab, (n_tab*5), n_tab, (n_tab*6), n_tab, (n_tab*7), n_tab, (n_tab*8), n_tab, (n_tab*9), n_tab, (n_tab*10)))
