"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.
"""

from math import trunc

print('\033[1;34mEscreva um número real para saber seu inteiro.')

n1 = float(input('\033[1;32mNúmero: '))

print(f'\033[1;34mO \033[1;32mnúmero\033[1;34m que você escreveu foi \033[1;32m{n1}\033[1;34m, Truncando esse número fica \033[1;32m{trunc(n1)}')
