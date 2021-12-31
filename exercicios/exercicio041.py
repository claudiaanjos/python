"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM;
- Até 14 anos: INFANTIL;
- Até 19 anos: JÚNIOR;
- Até 25 anos: SÊNIOR;
- Acima: MASTER.
"""

from datetime import date
nascimento = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('O atleta tem {} anos.\nClassificação: '.format(idade), end='')
if idade <= 9:
    print('MIRIM.')
elif idade <= 14:
    print('INFANTIL.')
elif idade <= 19:
    print('JÚNIOR.')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
