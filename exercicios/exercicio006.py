"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""

from math import sqrt

n1 = float(input('\033[1;34mEscreva um número para saber seu \033[1;33mdobro\033[1;34m, \033[1;35mtriplo \033[1;34me \033[1;36mraiz quadrada: '))

print(f'\n\033[1;33mDobro: {n1*2}')
print(f'\033[1;35mTriplo: {n1*3}')
print(f'\033[1;36mRaiz Quadrada: {sqrt(n1):.3f}')
