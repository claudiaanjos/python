"""
Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
"""

largura = float(input('\033[1;30mLargura da parede em metros: '))
altura = float(input('Altura da parede em metros: \033[m'))
área = largura * altura
tinta = área / 2

print('A parede tem uma área de \033[1;34m{}m²\033[m.'.format(área))
print('A quantidade de tinta necessária para pintar essa parede é de \033[1;31m{} litros.'.format(tinta))
