"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import date
s = (str(input('Qual o seu sexo? Digite \"F\" para feminino e \"M\" para masculino: '))).strip().upper()
if s == 'M':
    nasc = int(input('\nAno de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    alistamento = nasc + 18
    print('\nQuem nasceu em {} tem {} ano(s) em {} e'.format(nasc, idade, ano), end=' ')
    if idade == 18:
        print('\033[32mdeve se alistar o quanto antes!')
    elif idade > 18:
        print('já deve ter se alistado há \033[1;30m{}\033[m ano(s).'.format(idade - 18))
        print('O alistamento foi em {}.'.format(alistamento))
    elif idade < 18:
        print('ainda faltam \033[1;34m{}\033[m ano(s) para o alistamento.'.format(18 - idade))
        print('O alistamento será em {}.'.format(alistamento))
elif s == 'F':
    print('\n\033[1;30mVocê não precisa fazer o alistamento obrigatório.')
else:
    print('\n\033[1;31mOpção inválida. Reinicie o programa e tente novamente digitando uma opção válida.')
