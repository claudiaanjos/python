"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

p = float(input('\033[32mQual o preço do produto? R$\033[m'))
print('O produto com o custo de \033[1;32mR${:.2f}\033[m, está'.format(p), end=' ')
print('com \033[1;35m5%\033[m de desconto na promoção. Seu custo será de \033[1;36mR${:.2f}\033[m.'.format(p * 0.95))
