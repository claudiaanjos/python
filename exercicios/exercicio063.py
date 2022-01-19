"""
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
Ex: 0 → 1 → 1 → 2 → 3 → 5 → 8
"""

print('—' * 26)
print(f'| {"Sequência de Fibonacci":22} |')  
print('—' * 26)

n = int(input('Quantos termos você quer mostrar? '))

c = termof = 0
faux = faux2 = 1

print('~' * 26)  # '~' * (n * 5)

while c < n:
    print(termof, end=' → ')
    termof = faux
    faux = faux2
    faux2 = termof + faux
    c += 1
print('FIM')

print('~' * 26)
