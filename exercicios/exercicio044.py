"""
Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- À vista dinheiro/cheque: 10% de desconto;
- À vista no cartão: 5% de desconto;
- Em até 2x no cartão: Preço normal;
- 3x ou mais no cartão: 20% de juros.
"""

vp = float(input('Qual o valor total das compras? R$'))
print('''\nFormas de pagamento\n
[ 1 ] À vista (dinheiro/cheque);
[ 2 ] À vista no cartão;
[ 3 ] 2x no cartão;
[ 4 ] 3x ou mais no cartão.''')
fp = int(input('\nDigite a forma de pagamento: '))
if fp == 1:
    print('\nO produto custará R${:.2f}.'.format(vp * 0.9))
elif fp == 2:
    print(f'O produto custará R${vp * 0.95:.2f}.')
elif fp == 3:
    print('O produto custará R${:.2f} em 2 parcelas de R${:.2f}.'.format(vp, vp / 2))
elif fp == 4:
    p = int(input('Quantas parcelas? '))
    print('\nO produto custará R${:.2f} em {} parcelas de R${:.2f}. '.format(vp * 1.2, p, vp * 1.2 / p))
else:
    print('\033[1;31m\nOpção inválida.')
