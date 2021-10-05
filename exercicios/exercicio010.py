"""
Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

print('\033[4;34mEscreva o tanto de reais que você tem na carteira para saber o tanto de dólares que você pode comprar nesse exato momento.\033[m')

cart = float(input('\033[1;32mCarteira: '))

print(f'\033[1;34mvocê pode comprar \033[1;32m{cart/3.27:.2f}$')
