"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

import math

print('\033[1;34mEscreva um ângulo para saber seu, seno ,cosseno e tangente ')
n = float(input(f'Ãngulo:'))

print(f'\033[1;31mSeno: {math.sin(math.radians(n)):.2f}')
print(f'\033[1;32mCosseno: {math.cos(math.radians(n)):.2f}')
print(f'\033[1;35mTangente: {math.tan(math.radians(n)):.2f}')
