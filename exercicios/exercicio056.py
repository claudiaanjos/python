"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
► A média de idade do grupo;
► Qual é o nome do homem mais velho;
► Quantas mulheres têm menos de 20 anos.
"""

idade = 0
mocasmenos20 = 0
soma_idade = 0
maioridadehomem = 0
nomevelho = ''
genero = ''

for p in range(4):
    print('\n', '-' * 4, f'{p + 1}ª PESSOA', '-' * 4)
    nome = input('Nome: ').strip()
    idade = input('Idade: ')
    genero = input('Gênero/Sexo [M/F]: ').strip()  
    if not idade.isnumeric():
        print('\nErro. \033[1;31mIdade\033[m e/ou gênero inválido(s).')
        break
    soma_idade += int(idade)
    if genero in 'Mm' and (int(idade) > maioridadehomem or p == 0):
        maioridadehomem = int(idade)
        nomevelho = nome
    elif genero in 'Ff' and int(idade) < 20:
        mocasmenos20 += 1
    else:
        if genero not in 'FfMm':
            print('\nErro. O gênero informado é inválido.')
            break

if idade.isnumeric() and genero in 'FfMm':
    media_idade = soma_idade / 4
    print(f'\nMédia de idade: {media_idade:.1f} anos.\n'
          f'O homem mais velho tem {maioridadehomem} anos e se chama {nomevelho}.')
    print(f'Quantidade de moças com menos de 20 anos: {mocasmenos20}.')
