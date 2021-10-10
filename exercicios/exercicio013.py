"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

n = str(input('\033[1;34mQual o nome do Funcionário? '))
s = float(input('\033[1;33mQual o salário de {}? R$\033[m'.format(n)))
r = s + (s * 15 / 100)  
print('O salário de \033[1;32mR${:.2f}\033[m do funcionário \033[1;36m{}\033[m com 15% de aumento ficará \033[1;36mR$'
      '{:.2f}\033[m.'.format(s, n, r))
