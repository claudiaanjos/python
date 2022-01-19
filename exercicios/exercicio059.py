"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""

from time import sleep

opcao = 4
n1 = n2 = p = 0

while opcao != 5:
    if opcao == 1:
        print(f'{n1} + {n2} = {n1 + n2}')
    elif opcao == 2:
        print(f'{n1} x {n2} = {n1 * n2}')
    elif opcao == 3:
        if n1 > n2:
            print(f'{n1} > {n2}')
        elif n2 > n1:
            print(f'{n2} > {n1}')
        else:
            print(f'{n1} = {n2}')
    elif opcao == 4:
        n1 = int(input('Digite um número: '))
        n2 = int(input('Digite outro número: '))
    else:  
        print('Erro. Tente novamente.')

    if p != 0:
        print('=-=' * 10)
        sleep(2)
    else:
        p += 1

    print('''
    [1] Somar;
    [2] Multiplicar;
    [3] Maior;
    [4] Novos números;
    [5] Sair do programa.
    ''')

    opcao = int(input('>>>> Digite a opção: '))
    if opcao == 5:
        print('\nFinalizando...')
        print('=-=' * 10)
        sleep(2)

print('Fim do Programa. Volte sempre!')
