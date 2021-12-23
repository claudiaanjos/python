"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1.250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""

s = float(input('\033[1;30mDigite o salário do funcionário: R$'))
print()
if s > 1250:
    t = 10
    a = s * 1.1  # s + (s * t / 100)
else:
    t = 15
    a = s * 1.15  # s + (s * t / 100)
print('\033[1;33mO salário do funcionário que era R${:.2f} vai aumentar em {}% para R${:.2f}.'.format(s, t, a))
