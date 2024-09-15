# n = 2
# for c in range(0, n):
#     n = int(input('n:'))
#     print(n)
# print('terminou')
'''
Programa que mostre na tela uma contagem regressiva para o estouro de fogos
de artifício, indo de 10 a 0, com uma pausa de 1 segundo entre eles.
'''
# from time import sleep
# for c in range(10, -1, -1):
#     print(c)
#     sleep(1)

'''
Programa que mostre na tela todos os numeros pares que estão no intervalo entre 1 e 50
'''
# for c in range(2, 51, 2):
#     print(c)

'''
Programa que calcule a soma entre todos os numeros impares que são múltiplos 
de três e que se encontram no intervalo de 1 até 500
'''
# soma = 0.0
# counter = 0
# for c in range(1, 501, 2): 
#     if c % 3== 0:
#         soma += c
#         counter +=1
    
# print(f'A soma de todos os {counter} solicitados é igual a {soma}')

'''
Faça um programa que leia um numero inteiro qualquer e mostre  na tela  a
sua tabuada com laço for
'''
# numero = int(input('Digite um numero para ver sua tabuada: '))
# print(10*'-')
# for c in range(1,11):
#     print(f'{numero} x {c:2} = {numero*c}')
# print(10*'-')

'''
Desenvolva um programa que leia seis números inteiros e que mostre a soma 
apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
'''
# n = 0
# soma = 0
# for c in range(0,6):
#     n = int(input('Digite un numero inteiro: '))
#     if n % 2 == 0:
#         soma += n
# print('soma = ', soma)

'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
mostre os 10 primeiros termos dessa progressão  
'''
# primeiro_termo = int(input('Digite o primeiro termo de uma progressão aritmética: '))
# razao = int(input('Digite a razão dessa PA: '))
# soma = 0
# for c in range(primeiro_termo, primeiro_termo + razao*10, razao):
#     print(c, end = '→')



# num = int(input('Digite um numero inteiro: '))
# n=0
# for c in range(1, num+1):
#     if num % c == 0:
#         n+=1
# if n == 2:
#     print('É primo!')
# else:
#     print('Não é primo.')

'''
Desenvolva um programa que leia uma frase qualquer e diga se ela é um palíndromo
desconsiderando os espaços
'''

# str = input("Texto: ").lower().strip()
# str_no_space = str.replace(' ','')
# #Outra solução possível é str_split = str.split() / str_join = ''.join(str_split)
# str_size = len(str_no_space)
# str_inversed = str_no_space[::-1]
# str_size_neg = -1
# # # for c in range(str_size-1, -1, -1):
# # #     str_inversed += str_no_space[c]
# if str_inversed == str_no_space:
#     print('Palíndromo.')
# else:
#     print('Não é Palíndromo.')

'''
Pessoas maiores de idade pela data de nascimento
'''
# cont = 0
# for c in range(0,7):
#     ano = int(input(f"Digite ano de nascimento da pessoa {c}: "))
#     if (2024 - ano) >= 18:
#         cont += 1
# print(f'{cont} pessoa(s) é(são) maior(es) de idade')

"""

"""
# peso_maior = 0
# peso_menor = 0
# for c in range(1, 6):
#     peso = int(input(f"Digite o peso da {c}ª pessoa: "))
#     if c ==1:
#         peso_menor = peso
#     if peso > peso_maior:
#         peso_maior = peso
#     elif peso < peso_menor:
#         peso_menor = peso
# print(f'O maior peso foi {peso_maior}')
# print(f'O menor peso foi {peso_menor}')

'''
'''
soma_idade = 0
idade_maior = 0
mulher_menor_vinte = 0
nome_mais_velho = ''
for c in range(0,4):
    nome = input("Nome: ").strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M]/[F]: ').upper().strip()
    soma_idade += idade
    if sexo == 'M' and idade > idade_maior:
        nome_mais_velho = nome
    if sexo =='F' and idade <20:
        mulher_menor_vinte +=1
print('Média das idades: ', soma_idade/4)
if nome_mais_velho !='':
    print('O homem mais velho é ', nome_mais_velho)
print('Qtde de mulheres com menos de 20 anos: ', mulher_menor_vinte)