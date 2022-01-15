"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
Ex:
APOS A SOPA
A SACADA DA CASA
A TORRE DA DERROTA
O LOBO AMA O BOLO
ANOTARAM A DATA DA MARATONA
"""

frase = str(input('Frase: ')).upper()
palavras = frase.split()
fraseJunta = ''.join(palavras)
inversoFraseJunta = fraseJunta[::-1]  
print(f'O inverso de {fraseJunta} é {inversoFraseJunta}.')
if fraseJunta == inversoFraseJunta:
    print('É um palíndromo.')
else:
    print('Não é um palíndromo.')
