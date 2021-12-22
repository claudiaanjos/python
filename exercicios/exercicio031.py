"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longes.
"""

d = int(input('\033[1;30mDigite a distância da viagem em Km: '))
print('\n\033[1;35mCom a distância de {}Km'.format(d), end=' ')
if d <= 200:
    p = 0.5 * d
else:
    p = 0.45 * d
print('o preço da viagem será de \033[1;32mR${:.2f}\033[m\033[1;34m.\nTenha uma boa viagem!'.format(p))
