"""
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

def escolha(var, inicio, fim):
    opcoes = list(range(inicio, fim + 1))
    while var not in opcoes:
        var = int(input('\nOpção: '))
        print()
        if var not in opcoes:
            print('\nErro, opção inválida. Tente novamente.')
    return var


print('''
    [1] Progressão Aritmética (PA);
    [2] Progressão Geométrica (PG).''')

opcao = 0
opcao = escolha(opcao, 1, 2)

primeiroTermo = int(input('\nPrimeiro termo: '))
razao = int(input('Razão: '))
termo = -1

print('''
    [1] Ver os 10 primeiros termos;
    [2] Ver o valor de um termo específico;
    [3] Escolher um alcance dos termos, de até 10 casas.''')

opcaoTermos = 0
opcaoTermos = escolha(opcaoTermos, 1, 3)
termos = []

if opcaoTermos == 1:  
    termo = 1
    if opcao == 1:  
        decimoTermo = primeiroTermo + (10 - 1) * razao
        for c in range(primeiroTermo, decimoTermo + razao, razao):  
            termos += [c]
            print(f'\033[1;31m{termo}º \033[1;32m{c}\033[m', end=' \033[1m→ ')
            termo += 1
        print('Acabou.')
        print(f'\nForam digitados {len(termos)} termos.')
    else:  
        valorTermo = primeiroTermo
        valorDecimoTermo = primeiroTermo * (10 - 1) ** razao
        while valorTermo < valorDecimoTermo + razao:
            print(f'\033[1;31m{termo}º \033[1;32m{valorTermo}\033[m', end=' \033[1m→ ')
            valorTermo *= razao
            termo += 1
        print('Acabou.')
elif opcaoTermos == 2:  
    while termo < 2:
        termo = int(input('\nTermo: '))
        if termo < 2:
            print('\nErro. Tente novamente.')
    print()
    termo -= 1
    if opcao == 1:  
        valorTermo = primeiroTermo + (razao * termo)
        print(f'O valor do {termo + 1}º termo é: {valorTermo}.\n')
        print(f'{valorTermo - razao}', end=' → ') 
        print(f'\033[31m{valorTermo}\033[m', end=' → ')
        print(f'{valorTermo + razao}')  

    else:  
        valorTermo = primeiroTermo * (razao ** termo)
        print(f'O valor do {termo + 1}º termo é: {valorTermo}.\n')
        print(f'{(valorTermo / razao):.0f}', end=' → ')  
        print(f'\033[31m{valorTermo}\033[m', end=' → ')
        print(f'{valorTermo * razao}')  

else:  
    casaInicialTermos = 0
    casaFinalTermos = 0
    while casaInicialTermos >= casaFinalTermos or ((casaFinalTermos - casaInicialTermos) > 11):
        casaInicialTermos = int(input('\nCasa inicial dos termos: '))
        casaFinalTermos = int(input('Casa final dos termos: '))
    print()
    termo = casaInicialTermos
    casaInicialTermos -= 1
    if opcao == 1:  
        termoInicial = primeiroTermo + (razao * casaInicialTermos)
        ultimoTermo = primeiroTermo + (razao * casaFinalTermos)
        for c in range(termoInicial, ultimoTermo, razao):
            termos += [c]
            print(f'\033[1;31m{termo}º \033[1;32m{c}\033[m', end=' \033[1m→ ')
            termo += 1
        print('Acabou.')
    else:  # opcao == 2 PG
        valorTermo = primeiroTermo * (razao ** casaInicialTermos)
        valorUltimoTermo = primeiroTermo * (razao ** casaFinalTermos)
        while valorTermo < valorUltimoTermo:
            termos += [valorTermo]
            print(f'\033[1;31m{termo}º \033[1;32m{valorTermo}\033[m', end=' \033[1m→ ')
            valorTermo *= razao
            termo += 1
        print('Acabou.')
    print(f'\nTotal termos escritos na tela: \033[1;34m{len(termos)}\033[m.')
