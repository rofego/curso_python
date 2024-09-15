'''
Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos 
números foram digitados e qual foi a soma entre eles(desconsiderando o flag)
'''
# cont = soma = 0
# while True:
#     n = int(input('Digite um número: '))
#     if n == 999:
#         break
#     soma += n
#     cont += 1
# print(f'Soma total: {soma}')
# print(f'Qtde de números digitados: {cont}')

'''
TABUADA
'''
# n = int()
# while True:
#     n = int(input('Digite um número(<0 para parar): '))
#     if n<0:
#         break
#     for i in range(0,11):
#         print(f'{n:^3} X {i:<2} = {n*i:<3}')

'''
Par ou Ímpar
'''
# from random import randint
# import os
# from time import sleep
# num_comp = randint(0,100)
# par_impar = ''

# while True:
#     print(f'{'Ímpar ou Par':^25}\n{'Você tem que adivinhar!':^25}')
#     num_entrada = int(input('Digite seu número: '))
#     par_impar = input('A soma do seu número com o númrero secreto é Par ou ímpar?[P/I]')
#     soma  = num_comp + num_entrada
    
#     if (num_entrada + num_comp)%2==0:
#         if par_impar in 'Pp':
#             print(f'Você acertou!')
#             sleep(2)
#             print(f'Número secreto: {num_comp}')
#             print(f'Soma: {soma}')
#             sleep(2)
#             os.system('cls')
#         else:
#             print(f'Você errou!')
#             sleep(2)
#             print(f'Número secreto: {num_comp}')
#             print(f'Soma: {soma}')
#             sleep(2)
#             os.system('cls')
#             break
#     else:
#         if par_impar in 'Ii':
#             print(f'Você acertou!')
#             sleep(2)
#             print(f'Número secreto: {num_comp}')
#             print(f'Soma: {soma}')
#             sleep(2)
#             os.system('cls')
#         else:
#             print(f'Você errou!')
#             sleep(2)
#             print(f'Número secreto: {num_comp}')
#             print(f'Soma: {soma}')
#             sleep(2)
#             os.system('cls')
#             break
# print('Jogo encerrado!')
        
'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar. No final, mostre:

'''
# lista_cadastro = list()
# dados = list()

# print(f'Lista de Cadastro!')
# while True:
#     dados.append(int(input('Idade: ')))
#     sexo = opcao = ' '
#     while sexo not in 'MF':
#         sexo = input('Sexo[M/F]: ').strip().upper()[0]
#     dados.append(sexo)     
#     lista_cadastro.append(dados[:])
#     dados.clear()
#     while opcao not in 'SN':
#         opcao = input('Quer continuar? [S/N] ').strip().upper()
#     if opcao in 'Nn':
#         break
# cont_maior_18 = 0
# cont_masc = 0
# cont_fem_men_20 = 0
# for pessoa in lista_cadastro:
#     if pessoa[0]>=18:
#         cont_maior_18 += 1
#     if pessoa[1] in 'M':
#         cont_masc += 1
#     if pessoa[1] in 'F' and pessoa[0]<20:
#         cont_fem_men_20 += 1
    
# print(f'{cont_maior_18} pessoas têm mais de 18 anos.')
# print(f'{cont_masc} homens foram cadastrados.')
# print(f'{cont_fem_men_20} mulheres tem menos de 20 anos.')
'''
lista de compra
'''
# lista_compra = list()
# dados = list()
# print('-'*40)
# print(f'{'SUPERMERCADO HOJE':^40}')
# print('-'*40)
# while True:
#     dados.append(input('Nome do Produto: ').strip().upper())     
#     dados.append(float(input('Preço: R$')))
#     lista_compra.append(dados[:])
#     dados.clear()
#     opcao = ' '
#     while opcao not in 'SN':
#         opcao = input('Quer continuar? [S/N] ').strip().upper()
#     if opcao in 'Nn':
#         break
# print(f'{'FIM DAS COMPRAS':.^40}')


# total = 0
# maior_mil = 0
# barato = list()
# for pos, prod in enumerate(lista_compra):
#     total += prod[1]

#     if pos == 0:
#         barato = prod[:]

#     elif prod[1]<barato[1]:
#         barato = prod[:]

#     if prod[1]>1000:
#         maior_mil += 1


# print(f'O total da compra foi R${total:.2f}')
# print(f'{maior_mil} produtos estão custando mais de R$ 1000.00')
# print(f'O produto mais barato foi {barato[0]} que custa {barato[1]:.2f}')

'''
Crie um programa que simule o funcionamento de um caixa eletrônico
'''

print('='*40)
print(f'{'BANCO PRIVATEV':^40}')
print('='*40)

valor = float(input('Qual valor você quer sacar? R$'))
total = valor
ced = 50
totced = 0

# if valor//50 != 0:
#     print(f'{valor//50} cédulas de R$50 ')
# if (valor%50)//20 != 0:
#     print(f'{(valor%50)//20} cédulas de R$20 ')
# if ((valor%50)%20)//10 != 0:
#     print(f'{((valor%50)%20)//10} cédulas de R$10 ',)
# if (((valor%50)%20)%10)//1 != 0:
#     print(f'{(((valor%50)%20)%10)//1} cédulas de R$1 ')

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break