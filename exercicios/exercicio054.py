"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
"""

from datetime import date
ano_atual = date.today().year
maiores = 0
menores = 0
print('\n\033[1mAnálise maioridade 21 anos\033[m\n')
for pessoa in range(1, 8):  
    nascimento = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - nascimento
    if idade >= 21:
        maiores += 1
    else:  #
        menores += 1
print(f'\nMaiores de idade: {maiores}.\nMenores de idade: {menores}.')
