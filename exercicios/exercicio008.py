"""
Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
"""

print(f'\033[1;34mEscreva  uma reta em \033[1;33mmetros\033[1;34m para saber a conversão para \033[1;32mcentímetros \033[1;34me \033[1;36mmilímetros. ')
metros = float(input('\033[1;33mReta em metros: '))
print(f'\033[1;32mCentímetros: {metros/100} ')
print(f'\033[1;36mMilímetros: {metros/1000}')
