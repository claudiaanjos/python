"""
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- Equilátero: Todos os lados iguais;
- Isósceles: Dois lados iguais;
- Escaleno: Todos os lados diferentes.
"""

r1 = float(input('\nDigite o comprimento da reta 1: '))
r2 = float(input('Digite o comprimento da reta 2: '))
r3 = float(input('Digite o comprimento da reta 3: '))
print('\nOs segmentos acima', end=' ')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('podem formar um triângulo', end=' ')
    if r1 == r2 == r3:
        print('Equilátero.')
    elif r1 != r2 != r3 != r1:
        print('Escaleno.')
    else: 
        print('Isósceles.')
else:
    print('não podem formar um triângulo.')
