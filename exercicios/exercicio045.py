"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""

from random import randint
from time import sleep
o = ('\033[1mPedra\033[m', '\033[1;30mPapel\033[m', '\033[1;36mTesoura\033[m')  
print('''\nSuas opções
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
u = int(input('\nSua escolha: '))  
pc = randint(0, 2)  
print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PO!\n')
print('-=' * 27)
print('Você escolheu {} e o computador escolheu {}.'.format(o[u], o[pc]))
print('-=' * 27)
if pc == u:
    print('\n\033[1;33mEmpate!')
elif pc == 0 and u == 2 or pc == 1 and u == 0 or pc == 2 and u == 1:
    print('\n\033[1;31mVocê perdeu!')
elif u == 0 and pc == 2 or u == 1 and pc == 0 or u == 2 and pc == 1:
    print('\n\033[1;32mVocê venceu!')
else:
    print('\033[1;31mOpção inválida. Tente novamente!')
