"""
Faça um programa que leia um número qualquer e mostre o seu fatorial.
Ex:
5! = 5x4x3x2x1 = 120
"""

n = numero = int(input('Digite o número que deseja ver o fatorial: '))
negativo = ''

if numero < 0:
    numero -= (numero * 2)
    negativo = '(-) '
    print(negativo, end='')

fatorial = 1
print(f'{numero}!', end=' = ') 
while numero > 0:
    print(numero, 'x ' if numero > 1 else '= ', end='')
    fatorial *= numero
    numero -= 1

if negativo != '':
    print(negativo, end='')

print(fatorial)
