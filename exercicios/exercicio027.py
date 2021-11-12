"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome
separadamente.
Ex:
Input - Ana Maria de Souza
Output - Primeiro = Ana; Último = Souza
"""

nome = (str(input('Digite o seu nome completo: ')).strip()).split()
primeiro = nome[0]
ultimo = nome[-1]
print('\n{}Primeiro nome: {}.'.format('\033[1;33m', primeiro))
print('{}Último nome: {}.'.format('\033[1;34m', ultimo))

