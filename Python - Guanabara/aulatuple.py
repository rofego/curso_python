lanche = 'Hambúrguer',
lanche+='Suco','Pizza'

print('-'*10)
for comida in lanche:
    print(comida)

print('-'*10)
for cont in range(0, len(lanche)):
    print(lanche[cont])
print('-'*10)
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} que está na posição {pos} no menu.')


print(sorted(lanche))


'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero a vinte
O programa deve ler um número pelo telcado(0~20) e mostrá-lo por extenso

'''
# import os
# numero_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete',\
#                   'oito','nove','dez','onze','doze','treze','quatorze','quinze',\
#                   'dezesseis','dezessete','dezoito','dezenove','vinte')
# while True:
#     numero_entrada = int(input('Digite um numero(0~20): '))
#     if numero_entrada>=0 and numero_entrada <=20:
#         print(f'{numero_entrada} por extenso é {numero_extenso[numero_entrada]}')
#     else:
#         print('Error!')
#     decisao = input('Continuar? [s] ou [n]: ')
#     os.system('cls')
#     if decisao =='n':
#         break
    
'''
Cire uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados 
b) Os últimos 4 colocados da tabela
c) Um lista com os times em ordem alfabética
d) Em que posição na tabela está a chapecoense 
'''
# brasileirao = ('Flamengo', 'Atletico Mineiro','Palmeiras','Chapecoense',
#                'Vasco','Corinthians','Fluminense','Atletico Paranaense',
#                'Santos','Botafogo','Bahia','Vitoria','Fortaleza',
#                'Sampaio Correia','Gremio','Internacional','Cruzeiro',
#                'Havaí','Portuguesa','Paysandu')
# for i in range(0,5):
#     print(f'{i+1} - {brasileirao[i]}')

# print('-'*10)
# for i in range(len(brasileirao)-4, len(brasileirao)):
#     print(f'{i-1} - {brasileirao[i]}')

# print('-'*10)
# for time in sorted(brasileirao,reverse=True):
#     print(time)

# print('-'*10)
# print(f'A Chapecoense está na posição {brasileirao.index('Chapecoense')+1}ª')

'''
Programa que vai gerar cinco numeros aleatorios e colocar em uma tupla
Depois disso, mostre a listagem de numeros gerados e tambem indique
o menor e o maior valor que estao na tupla
'''
# import random

# tupla_aleat = (random.randint(0,1000),random.randint(0,1000),
#                random.randint(0,1000),random.randint(0,1000),
#                random.randint(0,1000))

# print(tupla_aleat)
# print(f'O valor mínimo da tupla é: {min(tupla_aleat)}')
# print(f'O valor máximo da tupla é: {max(tupla_aleat)}')

'''
Desenvolvar um programa que leia quatro valores pelo teclado e guarde-os
em uma tupla. No final, mostre:
A) Quantas vezes o valor 9
B) Em que posição digitou-se o primeiro valor 3
C) Quais foram os numeros pares

'''
# valores = ()
# pares = []
# n = 0
# count = 0
# for i in range(0,4):
#     valores += int(input('Digite um numero de 0~10: ')),

# print(f"O número 9 apareceu {valores.count(9)} vezes")
# if 3 in valores:
#     print(f'O primeiro valor 3 está na posição {valores.index(3)+1}ª')
# else:
#     print('Não tem 3 em valores.')
# for i in valores:
#     if i%2==0:
#         pares.append(i)
# print(f'Quais foram os numeros pares {pares}')
'''
Listagem de preços
'''
# prod_preco = ('Leite', 4.5,'Pão',0.8,'Café', 4.0,'Água', 6.0,'Arroz',3.4,'Feijão',4.5)
# print('-'*30)
# titulo = 'LISTAGEM DE PREÇOS'
# print(f'{titulo:^30}')
# print('-'*30)
# for i in range(0,len(prod_preco),2):
#     print(f'{prod_preco[i]:.<20}R$ {prod_preco[i+1]:>4.2f}')
# print('-'*30)
'''
numa tupla com varias paravras, o programa deve dizer as vogais de cada palavra
'''
# palavras = 'Refrigerante','Peso','Pizza','Carro','Viagem','Salgado','Medo','Parceiro','Picanha'

# for palavra in palavras:
#     print(f'Na palavra {palavra} temos ', end='')
#     for i in palavra.lower():
#         if i in 'aeiou':
#             print(i, end=' ')
#     print('')    
    
