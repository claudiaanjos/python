"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""


[print(num, end=', ' if num != 50 else '.') for num in range(2, 51, 2)]
