"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

a = input('\033[1;34mDigite algo: ')
print()
print('\033[30mTipo primitivo de {} é {}'.format(a, type(a)))
print('\033[33m{} é alfabético? {}'.format(a, a.isalpha()))
print('\033[35m{} é alfanumérico? {}'.format(a, a.isalnum()))
if a.isalpha():
    print('\033[1;34m{} está em minúsculas? {}'.format(a, a.islower()))
    print('\033[1;31m{} está em maiúsculas? {}'.format(a, a.isupper()))
    print('\033[1;32m{} está capitalizada? {}'.format(a, a.istitle()))
else:
    print('\033[31m{} é numérico? {}'.format(a, a.isnumeric()))
    print('\033[32m{} é só espaço? {}'.format(a, a.isspace()))
