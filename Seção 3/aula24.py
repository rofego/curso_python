#Operadores in e not in
# Strings são interáveis
# 0 1 2 3 4 5
# R o m u l o
#-6-5-4-3-2-1

# nome='Romulo'
# print(nome[3])
# print(nome[-5])

nome = input('Nome: ') or 'Vacilo'
encontrar = input('O que vc deseja encontrar? ')
if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')

