'''
Faça uma lista de compras com listas.
O usuário deve ter a possibilidade de inserir, apagar e listar
valores da sua lista.
NÃO PERMITA que o programa quebre com ERROS DE ÍNDICE INEXIsTENTES
na lista
'''
import os
entrada=''
produto =''
indice =''
compras = []
while True:
    print(30*'-')
    print('Selecione uma opção:')
    entrada=input(('[i]nserir [a]pagar [l]istar: '))
    
    if entrada =='i':
        os.system('cls')
        produto = input('Qual o produto a ser comprado? ')
        compras.append(produto)

    if entrada=='a':
        try:
            os.system('cls')
            indice = int(input('Digite o indice do produto a ser apagado: '))
            tamanho = len(compras)
            del compras[indice]
        except ValueError:
            print('Digite apenas numeros')
        except IndexError:
            print('Indice não existe')

        # if len(compras)!=0:
        #     os.system('cls')
        #     indice = int(input('Digite o indice do produto a ser apagado: '))
        #     tamanho = len(compras)
        #     if indice>=0 and indice<tamanho:
        #         compras.pop(indice)
        #     else:
        #         print('Esse indice não EXISTE. TENTE OUTRA VEZ')
        # if len(compras)==0:
        #     os.system('cls')
        #     print('Não há nada para apagar. LISTA VAZIA.')
        
    if entrada == 'l':
        os.system('cls')
        print(f'{'LISTA DE COMPRAS:':^30}')
        for i, prod in enumerate(compras):
            print(f'{i} {prod}')
    if entrada =='b':
        break
