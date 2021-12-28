"""
Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
- 1 para binário;
- 2 para octal;
- 3 para hexadecimal.
"""

n = int(input('\nDigite um número inteiro: '))
print('''\nEscolha uma das bases para conversão:\n
\033[1;32m[ 1 ]\033[m Converter para \033[1;32mBINÁRIO\033[m;
\033[1;34m[ 2 ]\033[m Converter para \033[1;34mOCTAL\033[m;
\033[1;35m[ 3 ]\033[m Converter para \033[1;35mHEXADECIMAL\033[m.''')

base = int(input('\nSua opção: '))

if base == 1:
    print('\n{} em \033[1;32mBINÁRIO\033[m é \033[1;32m{}\033[m.'.format(n, bin(n)[2:]))
elif base == 2:
    print('\n{} em \033[1;34mOCTAL\033[m é \033[1;34m{}\033[m.'.format(n, oct(n)[2:]))
elif base == 3:
    print('\n{} em \033[1;35mHEXADECIMAL\033[m é \033[1;35m{}\033[m.'.format(n, hex(n)[2:]))
else:
    print('\n\033[1;31mOpção inválida. Tente novamente.')
