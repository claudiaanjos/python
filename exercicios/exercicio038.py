"""
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
- O primeiro valor é maior;
- O segundo valor é maior;
- Não existe valor maior, os dois são iguais.
"""

n1 = int(input('\nDigite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
print()
if n1 > n2:
    print('O \033[31mprimeiro valor\033[m é \033[34mmaior\033[m.')
elif n2 > n1:
    print('O \033[31msegundo valor\033[m é \033[34mmaior\033[m.')
else:
    print('\033[31mNão existe\033[m valor maior, os dois valores são \033[34miguais\033[m.')
