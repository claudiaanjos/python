"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
"""

nome = str(input('\033[1;36mEscreva o nome de alguma pessoa: ')).upper()

print(f'\033[0;32mO nome dessa pessoa tem \033[1;32mSilva?: \033[m{"SILVA" in nome}')
