# num = [2, 5, 2, 9, 1]
# num[3] = 3
# num.append(7)
# num.sort(reverse=True)
# num.insert(2, 2)
# print(num)
# while 2 in num:
#     num.remove(2)
# print(num)
# print(f'Essa lista tem {len(num)} elementos')

# values = []
# for cont in range(0,5):
#     values.append(int(input('Digite um valor: ')))
# for pos, val in enumerate(values):
#     print(f'Na posição {pos} encontrei {val}!')

# a = [2, 3, 4, 7]

'''
Faça um programa que leia 5 valores numericos e guarde-os em uma lista
No final, mostre qual foi o maior e o menor valor digitado e a suas respectivas posições
'''

# valores = []

# for i in range(0,5):
#     valores.append(int(input(f'Digite um valor para a posição {i}: ')))
# print('-='*25)

# print(f'O maior valor foi {max(valores)} e está nas posições ', end='')
# for pos, val in enumerate(valores):
#     if val == max(valores):
#         print (f'{pos}...', end='')

# print('')

# print(f'O menor valor foi {min(valores)} e está nas posições ', end='')
# for pos, val in enumerate(valores):
#     if val == min(valores):
#         print (f'{pos}...', end='')

'''
Crie um programa onde o usuário possa digitar vários valores numéricos e
cadastre-os em uma lista.
Caso o número já exista lá dentro, ele NÃO SERÁ ADICIONADO
No final serão exibidos todos os valores únicos digitados em ORDEM CRESCENTE
'''
# valores =[]
# valor = 0
# continuar = ''
# while True:
#     valor = int(input('Digite um valor: '))
#     if valor not in valores:
#         valores.append(valor)
#         print(f'{valor} foi adicionado.')
#     else:
#         print('Valor duplicado! Não vou adicionar...')
#     continuar = input('Quer continuar? [S/N]')
#     if continuar in'Nn':
#         break
# print('-='*30)
# valores.sort()
# print(f'Você digitou os valores {valores}')

'''
Crie um programa onde o usuario possa digitar 5 VALORES NUMÉRICOS 
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar sort())
No final, mostre a lista ordenada na tela
'''

# valores = list()
# valor = 0
# for i in range(0,5):
#     if i==0:
#         valores.append(int(input('Digite um numero para adicionar na lista: ')))
#         print('Adicionado na lista.')
#     else:
#         valor = int(input('Digite um numero para adicionar na lista: '))
#         for j in range(0,i+1):
#             try:
#                 if valor > valores[j]:
#                     continue
#                 else:
#                     valores.insert(j,valor)
#                     print(f'Adicionado na posição {j} da lista.')
#                     break
#             except IndexError:
#                 valores.append(valor)
#                 print('Adicionado no final da lista!')
#                 break
# print(valores)                    
    
'''
Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, mostre:
A) Quantos números foram digitados 
B)A lista de valores ordenada de forma descrescente
C) Se o valor 5 foi digitado e está ou não na lista
'''

# valores = []

# while True:
#     valor = int(input('Digite um valor: '))
#     valores.append(valor)
#     print(f'{valor} foi adicionado.')
#     continuar = input('Quer continuar? [S/N]')
#     if continuar in'Nn':
#         break
# print('-='*30)
# print(f'Foram digitados {len(valores)} numeros')
# valores.sort(reverse=True)
# print(f'Os valores digitados decrescentemente: {valores}')
# if 5 in valores:
#     print('O valor 5 está na lista.')
# else:
#     print('Não tem 5 na lista.')

'''
Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os ímpares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
'''
# valores = []
# while True:
#     valor = int(input('Digite um valor: '))
#     valores.append(valor)
#     print(f'{valor} foi adicionado.')
#     continuar = input('Quer continuar? [S/N]')
#     if continuar in'Nn':
#         break
# valores_pares=[]
# valores_impares = []

# for val in valores:
#     if val%2==0:
#         valores_pares.append(val)
#     else:
#         valores_impares.append(val)
# print(f'Lista digitada: {valores}')
# print(f'Lista dos pares: {valores_pares}')
# print(f'Lisda dos impares: {valores_impares}')

'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
na ordem correta
'''

expressao = input('Digite sua expressão: ')
parenteses_1=0
parenteses_2=0
for i in expressao:
    if i=='(':
        parenteses_1+=1
    elif i==')':
        parenteses_2+=1

if parenteses_1==parenteses_2:
    print('Expressão com os parenteses em pares corretamente.')
elif parenteses_1!=parenteses_2:
    print('Expressão com a incorreta disposição de parenteses.')
