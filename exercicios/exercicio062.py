"""
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
"""


print('-=' * 10)
print(f'|{"Gerador de PA":^18}|')
print('-=' * 10)

primeiroTermo = int(input('\nPrimeiro termo da PA: '))
razao = int(input('Razão: '))

termo = primeiroTermo
c = 0

numtermos = 10

while c < numtermos:
    print(termo, end=' → ')
    termo += razao
    c += 1
    if c == numtermos:
        print('PAUSA')
        numtermos += int(input('\nQuantos termos a mais você quer mostrar? '))
print(f'\nProgressão finalizada c/ {numtermos} termos mostrados.')

