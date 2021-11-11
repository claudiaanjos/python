"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
"""

n = str(input('\033[31mEscreva o nome de alguma cidade: ')).split()[0]

print(f'\033[34mA cidade começa com Santo?:\033[m {"SANTO" in n.upper()}')
