"""
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A";
- Em que posição ela aparece a primeira vez;
- Em que posição ela aparece a última vez.
"""

frase = str(input('\033[1;30mDigite uma frase: ').strip()).upper()
a = frase.count('A')

pv = frase.find('A') + 1
uv = frase.rfind('A') + 1

print('\n\033[1;31mQuantas vezes a letra A aparece na frase: {}.'.format(a))
print('\033[1;36mPosição em que a letra A aparece pela primeira vez na frase: {}.'.format(pv))
print('\033[1;35mPosição em que a letra A aparece pela última vez na frase: {}.'.format(uv))

