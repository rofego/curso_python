"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado,
peça a digitação novamente até ter um valor correto
"""

# sexo = ''
# while sexo != 'M' and sexo != 'F':
#     print('Digite um sexo válido.\n')
#     sexo = input('Digite seu sexo: ').strip().upper()[0]
# print(f'Você digitou {sexo}.')

'''
Melhore o jogo do desafio 028 onde o computador vai "pensar" em um número de 0 a 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
foram necessários para vencer.
'''

# from random import randint
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m',
#          'pretoebranco':'\033[7;30m',
#          'boldazulverm':'\033[1;36;41m',
#          'boldverdbran':'\033[1;32;40m',
#          'boldbranverd':'\033[1;30;42m',
#          'noneverdpret':'\033[7;32m',
#          'acertou':'\033[1;30;42m',
#          'entrada':'\033[0;30;43m'}
# num_secreto = randint(0,10)
# tentativa = int()
# right = False
# while not right:
#     print(f'{cores['entrada']}')
#     tentativa = int(input(f'Digite sua tentativa: '))
#     if tentativa == num_secreto:
#         right = True
#     else:
#         if tentativa > num_secreto:
#             print('Menos...')
#         elif tentativa < num_secreto:
#             print('Mais...')
# print(f'Você acertou!! O numero  {cores['limpa']} {cores["acertou"]} {tentativa} {cores['limpa']} {cores['entrada']} é igual ao numero {num_secreto} do computador. {cores['limpa']}')

'''
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior 
[4] novos números
[5] sair do programa

seu programa deverá realizar a operação solicitada em cada caso
'''
# import os
# from time import sleep
# soma = 0
# mult = 0
# maior = 0
# calc = True
# while calc:
#     try:
#         num1 = int(input('Digite um número: '))
#         num2 = int(input('Digite outro número: '))
#     except ValueError:
#         print('Por favor, apenas números inteiros.')
#         continue
#     while True:
#         sleep(3)
#         print(f'Primeiro Número: {num1}')
#         print(f'Segundo Número: {num2}')
#         print('Menu: \n[1] Somar \n[2] Multiplicar \n[3] Maior \n[4] Novos Números \n[5] Sair do Programa')
#         opcao = input('Digite o numero da opção desejada: ')
#         os.system('cls')
#         if opcao not in '12345':
#             print('Entre uma opção válida.')
#             continue
#         opcao = int(opcao)
#         if opcao == 1:
#             soma = num1 + num2
#             print(f'Soma: {soma}')
#         elif opcao == 2:
#             mult = num1 * num2
#             print(f'Multiplicação: {mult}')
#         elif opcao == 3:
#             maior = num1
#             if num2>num1:
#                 maior = num2
#             print(f'Maior: {maior}')
#         elif opcao == 4:
#             break
#         elif opcao == 5:
#             calc = False
#             break

'''
Faça um programa que leia um número qualquer e mostre seu fatorial.
Ex.: 5! = 5*4*3*2*1 = 120
'''
# from math import factorial

# num = int(input('Digite um número: '))
# num_fat = factorial(num)
# print(f'O fatorial de {num} é igual a {num_fat}')

# num = int(input('Digite um número: '))
# num_fat = 1
# count = num
# while count>0:
#     num_fat *= count
#     count-=1
# print(f'O fatorial de {num} é igual a {num_fat}')

# num = int(input('Digite um número: '))
# num_fat = 1
# for i in range(1, num+1):
#     num_fat *= i
# print(f'O fatorial de {num} é igual a {num_fat}')

'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão
usando a estrutura while
'''
# prim_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razao: '))
# x = 1
# print('PA: ', end='')
# termo_x = prim_termo
# while x<=10:
#     print(f'{termo_x}, ' if x<10 else f'{termo_x}.',end='')
#     termo_x += razao
#     x+=1
# print()
# print('FIM')

'''
Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos
'''
# prim_termo = int(input('Digite o primeiro termo da PA: '))
# razao = int(input('Digite a razao: '))
# x = 1
# count = 1

# termo_x = int()
# while x != 0:
#     x = int(input('Digite a qtde de termos(0 para encerrar): '))
#     termo_x = prim_termo
#     print('PA: ', end='')
#     count = 1
#     while count<=x:
#         print(f'{termo_x}, ' if count<(x) else f'{termo_x}.',end='')
#         termo_x += razao
#         count+=1
#     print()
# print()
# print('FIM')

'''
Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma
sequência de Fibonacci
'''
# n_vezes = int(input('Digite um número inteiro: '))
# soma = 1
# segun = 1
# prim = 0
# count = 0
# while count <n_vezes:
#     print(f'{soma}->',end='')
#     soma = prim + segun
#     prim = segun
#     segun = soma
#     count +=1
# print('FIM')

'''
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor
999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi  a soma entre eles
(desconsiderando o flag)
'''
# x = 0
# soma = 0
# count = -1
# while x!=999:
#     soma += x
#     count +=1
#     x = int(input('Digite um número(999 para encerrar): '))
# print(f'Foram digitados {count} números e a soma deles é {soma}.')

'''
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos
os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar valores
'''

num = int()
mai = men = med = count = 0
while True:
    num = int(input('Digite um número: '))
    med += num
    if count == 0:
        mai = men = num
    if num > mai:
        mai = num
    elif num < men:
        men = num
    count +=1
    opcao = input('Quer continuar? [S/N] ')
    if opcao in 'Nn':
        break
    
med /= count
print('Média: {}\n Maior: {}\n Menor: {}'.format(med,mai,men))




