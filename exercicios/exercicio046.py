"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
"""

from time import sleep
from emoji import emojize

print('\n\033[1;30mContagem regressiva para o estouro dos fogos de artíficio.\033[m\n')
for c in range(10, -1, -1):
    sleep(1), print(c)
print('\n\033[1;33mBOOM, POW, PA, PE, (...)!\033[1;35m', end='      ')
for r in range(10):
    print(emojize(':fireworks:       '), end='')
print()
