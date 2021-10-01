"""
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
"""

from time import sleep

print('\033[1;34mEscreva as notas que o aluno teve para saber a média máxima de 10. ')
sleep(1)
n1 = float(input('\033[1;34mPrimeira nota: '))
n2 = float(input('Segunda nota: '))

if (n1+n2)/2 == 10:
    print(f'\033[1;32mSua nota foi {(n1+n2)/2}. Parabéns! Você conseguiu nota máxima. ')

elif (n1+n2)/2 >= 6:
    print(f'\033[1;33mSua nota foi {(n1+n2)/2}. Parabéns! Você consegiu a nota média. estude um pouco mais para conseguir a nota máxima')

else:
    print(f'\033[1;31mSua nota foi {(n1+n2)/2}. Sua nota não foi tão boa, estude mais para conseguir uma nota melhor. ')
