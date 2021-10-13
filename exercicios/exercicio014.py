"""
Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

print('\033[1;34mConversor de Temperatura de Celsius para Fahrenheit. Qual valor em Celsius quer converter?')

GC = float(input('\033[1;31mGraus Celsius: '))

print(f'\033[1;34mConvertendo os \033[1;31mgraus celsius\033[1;34m para \033[1;31mfehrenheit \033[1;34mfica: \033[1;31m{(GC * 9/5) + 32}°F')
