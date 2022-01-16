"""
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

computador = randint(0, 10)

acertou = False

tentativas = 0

while not acertou:
    jogador = int(input('\nTente adivinhar o nº escolhido pelo computador entre 0 e 10: '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais...', end=' ')
        else: 
            print('Menos...', end=' ')
        print('Tente outra vez.')

print(f'Acertou com {tentativas} tentativas. Parabéns!')
