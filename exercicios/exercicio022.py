"""Crie um programa que leia o nome completo de uma pessoa e mostre:
– O nome com todas as letras maiúsculas e minúsculas.
– Quantas letras ao todo (sem considerar espaços).
– Quantas letras tem o primeiro nome.
"""

import time

# Cores: preto, Vermelho, Verde, Amarelo, Azul, Roxo, Ciano e Cinza
cor = ['\033[30m','\033[31m','\033[32m', '\033[33m', '\033[34m', '\033[35m', '\033[36m', '\033[37m',]
# Estilos: Negrito, Underline e Negativo
estilo = ['\033[1m', '\033[4m', '\033[7m']

print(f'\n{cor[4].__add__(estilo[0])}Escreva o seu {cor[1]}nome {cor[4]}para analisar-lo.')
n = str(input(f'{cor[1]}Nome: '))
time.sleep(1)
print(f'\nNome {cor[4]}completo em:\n\n\033[0mMaiúsculo: {n.upper()}\nMinúsculas: {n.lower()}\n=-----------')
print(f'Número de letras: {len(n.replace(" ",""))} ')
n1 = n.split()
print(f'Número de letras do primeiro nome: {len(n1[0])}')
