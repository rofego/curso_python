# from math import erf #Ctrl + Space Bar
# numero = int(input('Digite um numero: '))
# raiz = sqrt(numero)

# print('A raiz de {} é {}'.format(numero, floor(raiz)))
# import emoji
# print(emoji.emojize('Estou preocupado :anguished_face:'))

'''
Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira
'''
# from math import floor
# numero = float(input('Digite o numero: '))
# numero_int = floor(numero)
# print('O número {} tem a parte inteira {}.'.format(numero, numero_int))

# numero = float(input('Digite o numero: '))
# numero_int = int(numero)
# print('O número {} tem a parte inteira {}.'.format(numero, numero_int))

'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
'''
# import math
# cat1 = float(input('Digite o cateto 1: '))
# cat2 = float(input('Digite o cateto 2: '))
# hip = math.hypot(cat1, cat2)
# print('A hipotenusa desse triângulo é: {:.2f}'.format(hip))

'''
Faça um programa que leia um ângulo qualquer e 
mostre na tela o valor do seno, cosseno e tangente desse ângulo
'''
# import math 
# angulo_graus = float(input('Digite o ângulo em °: '))
# angulo_rad = math.radians(angulo_graus)
# seno = math.sin(angulo_rad)
# coss = math.cos(angulo_rad)
# tang = math.tan(angulo_rad)
# print(f'Seno: {seno:.2f}')
# print(f'Cosseno: {coss:.2f}')
# print(f'Tangente: {tang:.2f}')
'''
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome delas e escrevendo o nome do escolhido
'''
# from random import choice
# alunos = []
# for i in range(0,4):
#     alunos.append(input(f'Nome do aluno {i+1}: '))
# print(f'O professor escolheu o aluno {choice(alunos)} para apagar o quadro')
'''
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
'''
# import random
# alunos = []
# for i in range(0,4):
#     alunos.append(input(f'Nome do(a) aluno(a) {i+1}: '))
# novordem = random.sample(alunos, len(alunos))
# print(f'A ordem ficou: ')
# for pos, aluno in enumerate(novordem):
#     print(f'{pos+1} - {aluno}')
# print(alunos)
# print('-'*30)

'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
'''
import pygame
pygame.init()
pygame.mixer.music.load('Downstream_70k.wav')
pygame.mixer.music.play()
input()
pygame.event.wait()
