"""
Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
"""

from time import sleep
print('\nAnalise o sucessor e antecessor de um número qualquer.')
print()
n = int(input('\033[1;33mDigite um número: '))
print('\033[1;35mNúmero {}{}\033[1;35m em análise...\033[m'.format(
    '\033[4;30m', n))
sleep(4)
s = '\033[1;31m{}\033[m'.format(n + 1)
a = '\033[1;36m{}\033[m'.format(n - 1)
print('\nO sucessor do número \033[32m{}\033[m é {}. E o antecessor é {} >>>'.format(
    n, s, a), end=' ')
print('{} - \033[32m{}\033[m - {}'.format(a, n, s))
