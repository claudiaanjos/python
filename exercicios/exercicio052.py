"""
Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""

numero = int(input('\nDigite um número: '))
divisores = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        print(f'\033[1;32m{c}', end=' ')
        divisores += 1
    else:
        print(f'\033[1;31m{c}', end=' ')
print(f'\n\033[mO número {numero} foi divisível {divisores} vezes.\nE por isso ele \033[1m', end='')
if divisores == 2:
    print('É PRIMO.')
else:
    print('NÃO É PRIMO.')
