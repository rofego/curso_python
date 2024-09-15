# galera = list()
# dado = list()
# totmai = 0
# totmen = 0
# for c in range(0,5):
#     dado.append(input('Nome: '))
#     dado.append(int(input('Idade: ')))
#     galera.append(dado[:])
#     dado.clear()

# print(f'dado: {dado} \n galera: {galera}')

# for pessoa in galera:
#     if pessoa[1]>=18:
#         print(f'{pessoa[0]} é maior de idade.')
#         totmai +=1
#     else:
#         print(f'{pessoa[0]} é menor de idade')
#         totmen -=1
# print(f'Temos {totmai} maiores de idade e {totmen} menores de idade.')

'''
Faça um programa que leia nome e peso de várias pessoas
guardando tudo em um lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Um listagem com as pessoas mais leves.

'''

# dados = list()
# banco_de_dados = list()
# opcao = ''
# peso_men = 0
# peso_mai = 0 

# while True:
#     dados.append(input('Nome: '))
#     dados.append(int(input('Peso: ')))
#     if len(banco_de_dados) == 0:
#         peso_men = dados[1]
#     else:
#         if dados[1] < peso_men:
#             peso_men = dados[1]
#         if dados[1]>peso_mai:
#             peso_mai = dados[1]
#     banco_de_dados.append(dados[:])
#     dados.clear()
#     opcao = input('Quer continuar? [s/n] ')
#     if opcao in 'Nn':
#         break
# print('-='*40)
# print(f'Ao todo, você cadastrou {len(banco_de_dados)} pessoas.')

    
# lista_maipeso = []
# lista_menpeso = []
# for nome, peso in banco_de_dados:
#     if peso_men == peso:
#         lista_menpeso.append(nome)
#     if peso_mai == peso:
#         lista_maipeso.append(nome)
# print(f'O maior peso foi de {peso_mai}Kg. Peso de {lista_maipeso}')
# print(f'O maior peso foi de {peso_men}Kg. Peso de {lista_menpeso}')

'''
Crie um programa onde o usuário possa digitar sete valores numéricos
e cadastre-os em uma lista única que mantenha separados os valores pares e impares.
No final, mostre os valores pares e impares em ordem crescente
'''

# princ = [[],[]]
# entrada = 0
# for i in range(0,7):
#     entrada = int(input(f'Digite o numero {i+1}/7: '))
#     if entrada%2==0:
#         princ[0].append(entrada)
#     else:
#         princ[1].append(entrada)
# princ[0].sort()
# princ[1].sort()
# print(f'Os valores pares digitados foram: {princ[0]}')
# print(f'Os valores ímpares digitados foram: {princ[1]}')

'''
Crie um programa que crie uma matriz de dimensão 3x3 e 
preencha com valores lidos pelo teclado
No final, mostre na tela, com a formatação correta 
'''
# matriz_3_x_3=[[0,0,0],[0,0,0],[0,0,0]]
# for i in range(0, 3):
#     for j in range(0, 3):
#         matriz_3_x_3[i][j] = int(input(f'l({i+1})c({j+1}):'))
# for i in range(0, 3):
#     for j in range(0, 3):
#         print(f'[{matriz_3_x_3[i][j]:^5}]', end='')
#     print()

'''
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados
b) A soma dos valores da terceira coluna
c) O maior valor da segunda linha
'''
# matriz_3_x_3=[[0,0,0],[0,0,0],[0,0,0]]
# mai_lin_2 = 0

# for i in range(0, 3):
#     for j in range(0, 3):
#         matriz_3_x_3[i][j] = int(input(f'l({i+1})c({j+1}):'))
#         if i == 1 and j == 0:
#             mai_lin_2 = matriz_3_x_3[i][j]
#         elif i == 1 and matriz_3_x_3[i][j]>mai_lin_2:
#             mai_lin_2 = matriz_3_x_3[i][j]

# soma_pares = 0
# soma_col_3 = 0
# print('-='*40)
# for i in range(0, 3):
#     for j in range(0, 3):
#         if matriz_3_x_3[i][j]%2==0:
#             soma_pares += matriz_3_x_3[i][j]
#         if j==2:
#             soma_col_3 += matriz_3_x_3[i][j]
       
#         print(f'[{matriz_3_x_3[i][j]:^5}]', end='')

#     print()
# print('-='*40)
# print(f'A soma de todos os valores pares da Matriz 3x3 é: {soma_pares}')
# print(f'A soma dos valores da coluna 3: {soma_col_3}')
# print(f'O maior valor da segunda linha: {mai_lin_2}')

'''
Faça um programa que ajude um jogador da MEGASENA a criar PALPITES. 
O programa vai perguntar QUANTOS JOGOS serão gerados e vai sortear 6 NÚMEROS ENTRE 1 E 60 para cada
jogo, cadastrando tudo em uma lista composta.
'''
import random
import time

# megasena = []
# qtde_jogos = 0
# print('-'*40)
# titulo = 'JOGA NA MEGA SENA'
# print(f'{titulo:^40}')
# print('-'*40)
# qtde_jogos = int(input('Quantidade de jogos: '))
# titulo_2=f'SORTEANDO {qtde_jogos} JOGOS'
# print('-'*40)
# print(f'{titulo_2:^40}')
# print('-'*40)

# aleat = 0
# for i in range(0, qtde_jogos):
#     megasena.append([])
#     while True:
#         aleat = random.randint(1,60)
#         if aleat not in megasena[i]:
#            megasena[i].append(aleat)
#         if len(megasena[i])==6:
#             break

        
#     megasena[i].sort()

# for i in range(0, qtde_jogos):
#     time.sleep(1)
#     print(f'Jogo {i+1}: ',end='')
#     time.sleep(1)
#     print('[ ',end='')
#     for j in range(0, 6):
#         time.sleep(1)
#         print(f'{megasena[i][j]:^3} ',end='')
#     time.sleep(1)
#     print(']')
# time.sleep(1)
# print('-'*40)
# time.sleep(1.5)
# print('BOA SORTE!')
# print()
# time.sleep(2)
# quit()

'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo
em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário
possa mostrar notas de cada aluno individualmente 
'''
import decimal
boletim = []
aluno = []
notas = []
med = 0.0
opcao = ''

while True:
    aluno.append(input('Nome: '))
    for i in range(0,2):
        notas.append(float(input(f'Nota {i+1}: ')))
    aluno.append(notas[:])
    med = (notas[0]+notas[1])/2
    aluno.append(med)
    notas.clear()
    med=0.0
    boletim.append(aluno[:])
    aluno.clear()  
    opcao = input('Quer continuar? [S/N] ')
    if opcao in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)

for pos, i in enumerate(boletim):
    print(f'{pos+1:<4}{i[0]:<12}{i[2]:^8.1f}')
print('-='*30)
entrada_aluno = 0
while True:
    entrada_aluno = int(input(f'Mostrar notas de qual aluno? (999 interrompe): '))
    entrada_aluno -= 1
    try:
        print(f'Notas de {boletim[entrada_aluno][0]} são {boletim[entrada_aluno][1]}')
    except:
        print('Error')
        if entrada_aluno == 999:
            break
print('-'*25)
# print(boletim)