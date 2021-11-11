"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

# Cores: preto, Vermelho, Verde, Amarelo, Azul, Roxo, Ciano e Cinza
cor = ['\033[30m','\033[31m','\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m',]

n = int(input(f'escreva um número de 4 digitos: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'{cor[3]}Milhar: {m}')
print(f'{cor[4]}Centena: {c} ')
print(f'{cor[6]}Dezena: {d}')
print(f'{cor[1]}Unidade: {u}')
