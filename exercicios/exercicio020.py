"""O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada."""

import random

print('\033[1;34mEscreva nome de 4 alunos para sortear a ordem.')

n1 = str(input('Aluno 1: '))
n2 = str(input('Aluno 2: '))
n3 = str(input('Aluno 3: '))
n4 = str(input('Aluno 4: '))

lista = [n1, n2, n4, n4]
random.shuffle(lista)
print(f'{lista}')
