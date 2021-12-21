"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

n = int(input('Tente adivinhar o número escolhido pelo computador de 0 a 5: '))
pc = randint(0, 5)  # Faz o computador "escolher"
if n == pc:
    print('\nParabéns você acertou o número e venceu!')
else:
    print('\nQue pena você errou, na próxima quem sabe?')
    print('\nO número escolhido foi: {}.'.format(n))
    print('O número sorteado foi: {}.'.format(pc))


