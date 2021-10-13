"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
"""

print('\033[1;34mEscreva quantos km o carro percorreu e a quantidade de dias que você alugou')

al = int(input('\033[1;34mQuantidade de dias: '))

km = float(input('\033[1;34mKm Percorrido: '))

print(f'\033[1;34mO \033[1;32mpreço \033[1;34mtotal deu: \033[1;32m{(al * 60) + ( km * 0.15)}R$')
