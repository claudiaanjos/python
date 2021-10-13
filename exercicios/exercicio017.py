"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot

print('\033[1;34mEscrevas 2 retas de um triângulo retângulo para saber o comprimento da hipotenusa. ')
n1 = float(input('Cateto oposto: '))
n2 = float(input('Cateto adjacente: '))

print(f'\033[1;31mHipotenusa: {hypot(n1, n2):.3f}')
