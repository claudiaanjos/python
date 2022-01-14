"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
"""

numerosPares = []
quantidadeNum = 0
while quantidadeNum > 10 or quantidadeNum < 1:
    quantidadeNum = int(input('\nQuantos números? '))
    if quantidadeNum > 10 or quantidadeNum < 1:
        print('\nErro. Tente novamente.')
print()
for c in range(quantidadeNum):
    n = [int(input(f'Digite o {c + 1}º número: '))]
    numerosPares += [i for i in n if i % 2 == 0]
print()
if len(numerosPares) > 1:
    print(f'Quantidade de pares: {len(numerosPares)}.\nSoma dos pares: {sum(numerosPares)}.')
    print(f'Os números pares foram: {numerosPares}.')
elif len(numerosPares) == 1:
    print(f'Você digitou apenas 1 número par que foi: {numerosPares}.')
else:
    print('Você não digitou nenhum número par.')
