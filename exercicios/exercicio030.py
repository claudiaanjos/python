"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

from time import sleep
n = int(input('Digite um número: '))
print('Analisando...\n')
sleep(1.2)
if n % 2 == 0:
    print('Este número é par.')
else:
    print('Este número é ímpar.')

