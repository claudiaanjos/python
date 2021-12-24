"""
Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
"""

r1 = float(input('\n\033[1;33mDigite o comprimento da reta 1: '))
r2 = float(input('\033[1;34mDigite o comprimento da reta 2: '))
r3 = float(input('\033[1;35mDigite o comprimento da reta 3: '))

if r1 + r2 <= r3 or r2 + r3 <= r1 or r3 + r1 <= r2:
    p = ' não '
else:
    p = ' '
print('\n\033[1;30mOs comprimentos acima{}podem formar um triângulo.'.format(p))
