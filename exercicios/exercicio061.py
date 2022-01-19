"""
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.
"""

print('-=' * 10)
print(f'|{"Gerador de PA":^18}|')
print('-=' * 10)

primeiroTermo = int(input('\nPrimeiro termo da PA: '))
razao = int(input('Razão: '))

termo = c = 0
while c < 10:  # termo < ultimoTermo
    termo = primeiroTermo + (razao * c)
    print(termo, end=' → ')
    c += 1

print('FIM')
