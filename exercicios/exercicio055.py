"""
Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""

peso_ma = 0
peso_me = 0  

print()
for p in range(5):
    peso = float(input(f'Digite o peso da {p + 1}ª pessoa: '))

    '''
    if p == 0:
        peso_me = peso
        peso_ma = peso
    '''

    if peso > peso_ma or p == 0:
        peso_ma = peso
    if peso < peso_me or p == 0:
        peso_me = peso

print('\nO menor peso lido foi {}Kg e o maior foi {}Kg.'.format(peso_me, peso_ma))
