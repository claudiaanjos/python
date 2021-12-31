"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso;
- Entre 18.5 e 25: Peso ideal;
- 25 até 30: Sobrepeso;
- 30 até 40: Obesidade;
- Acima de 40: Obesidade mórbida.
"""

peso = float(input('Peso (Kg): '))
altura = float(input('Altura (metros):  '))
imc = peso / (altura ** 2)  
print('\nIMC = {:.1f}\nCondição: \033[1;30m'.format(imc), end='')
if imc < 18.5:
    p = 'Abaixo do peso'
elif imc < 25:
    p = 'Peso ideal'
elif imc < 30:
    p = 'Sobrepeso'
elif imc < 40:
    p = 'Obesidade'
else:
    p = 'Obesidade mórbida\033[1;31m\n\nCondição de risco! Tome cuidado.'
print(p)
