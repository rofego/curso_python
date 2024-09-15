# dados = dict()
# dados = {'nome':'Pedro', 'idade':18}
# print(dados['nome'])
# print(dados['idade'])
# dados['sexo'] = 'M'

# print(dados)
# del dados['idade']

# print(dados)

# filme = {'titulo':'Star Wars',
#          'ano':1977,
#          'diretor':'George Lucas'
#          }

# print(filme.values())
# print(filme.keys())
# print(filme.items())

# for key,val in filme.items():
#     print(f'O {key} é {val}')

# estado = dict()
# brasil = list()
# for c in range(0, 3):
#     estado['uf'] = input('Unidade Federativa: ')
#     estado['sigla'] = input('Sigla do Estado: ')
#     brasil.append(estado.copy())

# for e in brasil:
#     print(e)

'''
Programa que leia nome e média de um aluno.
guardando também a situação em um dicionário.
mostre essa estrutura na tela
'''

# aluno = dict()

# aluno['Nome'] = input('Nome: ')
# aluno['Média'] = float(input('Média: '))
# if aluno['Média'] < 7:
#     aluno['Situação'] = 'reprovado'.title()
# else:
#     aluno['Situação'] = 'aprovado'.title()

# for k, v in aluno.items():
#     print(f'{k} é igual a {v}')

'''
Crie um programa onde 4 jogadores joguem um dado e tenham
resultados aleatórios. guarde esses resultados em um dicionário.
Coloque o dicionário em ordem, o vencedor tirou o maior número no dado
'''
# from random import randint
# from time import sleep
# # lance = dict()
# # rodada = list()
# # print('Valores sorteados: ')
# # for i in range(0,4):
# #     lance['nome'] = 'jogador'+f'{i+1}'
# #     lance['dado'] = randint(1,6)
# #     if i==0:
# #         rodada.append(lance.copy())
# #     else:
# #         cont = 0
# #         for j in range(0,len(rodada)):
# #             if lance['dado']>rodada[j]['dado']:
# #                 cont += 1
# #                 rodada.insert(j, lance.copy())
# #                 break
# #         if cont == 0:
# #             rodada.append(lance.copy())
                
# #     sleep(1)
# #     print(f'O {lance["nome"]} tirou {lance["dado"]}')

# # print('Ranking dos jogadores: ')
# # for i in range(0,4):
# #     sleep(1)
# #     print(f'{i+1}º lugar: {rodada[i]["nome"]} com {rodada[i]["dado"]}')
# from operator import itemgetter
# jogo = {'jogador1':randint(1, 6),
#         'jogador2':randint(1, 6),
#         'jogador3':randint(1, 6),
#         'jogador4':randint(1, 6)}
# ranking = dict()
# print('Valores sorteados:')
# for k, v in jogo.items():
#     sleep(1)
#     print(f'{k} tirou {v} no dado.')

# ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
# print('Ranking dos jogadores: ')
# for pos, jogo in enumerate(ranking):
#     sleep(1)
#     print(f'{pos+1}º Lugar - {jogo[0]} que tirou {jogo[1]} nos dados.')

'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionário.
Se por acaso o CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
# import datetime

# data_de_hoje = datetime.date.today().year
# print(data_de_hoje)

# funcionario = {}
# funcionario['Nome'] = input('Nome: ')
# ano_nasc = int(input('Ano de nascimento: '))
# funcionario['Idade'] = data_de_hoje - ano_nasc
# funcionario['CTPS'] = int(input('CTPS(digite "0" se não tem): '))
# ano_contrat = int()
# salario = float()
# if funcionario['CTPS'] != 0:
#     funcionario['Ano de Contratação'] = int(input('Ano de contratação: '))
#     funcionario['Salário'] = float(input('Salário: R$'))
# funcionario['Aposentadoria'] = (funcionario['Ano de Contratação']+35)-(data_de_hoje-funcionario['Idade'])
# for k, v in funcionario.items():
#     print(f'{k} é igual a {v}')


# print(funcionario)

'''
Ler nome do jogador, qtde de partidas jogadas. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''
# aproveitamento = dict()
# gols_partida = list()
# aproveitamento['Nome'] = input('Nome: ')
# partidas_jogadas = int(input(f'Qtde de partidas jogadas por {aproveitamento["Nome"]}: '))
# for i in range(0, partidas_jogadas):
#     gols_partida.append(int(input(f'Quantidade de gols feitos na partida {i+1}: ')))

# aproveitamento['gols'] = gols_partida
# aproveitamento['gols_total'] = sum(gols_partida) 
# print('=-'*25)
# print(aproveitamento)
# print('=-'*25)
# for k, v in aproveitamento.items():
#     print(f'O campo {k} tem valor {v}.')
# print('=-'*25)

# print(f'O jogador {aproveitamento['Nome']} jogou {len(aproveitamento['gols'])} partidas.')
# for pos, val in enumerate(aproveitamento['gols']):
#     print(f'=> Na partida {pos+1}, fez {val} gols.')
# print(f'Fez um total de {aproveitamento['gols_total']} gols.')
# print('=-'*25)

'''
Crie um programa que leia nome, sexo, e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
    A) Quantas pessoas foram cadastradas
    B) A média de idade do grupo
    C) Uma lista com todas as mulheres
    D) Uma lista com todas as pessoas com idade acima da média
'''
# import os
# banco = list()
# pessoa = dict()
# banco_femin = list()
# med = 0
# while True:
#     pessoa['Nome'] = input('Nome: ')

#     while True:
#         pessoa['Sexo'] = input('Sexo; [M/F]').strip().upper()[0]
#         if pessoa['Sexo'] in 'MF':
#             break
#         else:
#             print('Error. Tente novamente.')
#     pessoa['Idade'] = int(input('Idade: '))

#     med += pessoa['Idade']
#     banco.append(pessoa.copy())
#     if pessoa['Sexo'] == 'F':
#         banco_femin.append(pessoa.copy())
#     continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
#     if continuar == 'N':
#         break

# # os.system('cls')
# print(f'{len(banco)}pessoas foram cadastradas.')

# med /= len(banco)
# print(f'Média da idade: {med}')

# print('=-'*20)
# print(f'Lista de todas as mulheres: ')
# for mulher in banco_femin:
#     print(f'{mulher['Nome']}')
# print('=-'*20)

# banco_idade_acima_med = list()
# for pessoa in banco:
#     if pessoa['Idade']>med:
#         banco_idade_acima_med.append(pessoa.copy())

# print('=-'*20)
# print(f'Lista de todas as pessoas com idade acima da média: ')
# print(banco_idade_acima_med)
# print('=-'*20)

'''
Quase semelhante ao exercício do aproveitamento, mas agora com um laço para pôr quantos jogadores quiser.
'''

aproveitamento = dict()
gols_partida = list()
jogadores = list()
partidas = list()
while True:
    aproveitamento['Nome'] = input('Nome: ')
    partidas_jogadas = int(input(f'Qtde de partidas jogadas por {aproveitamento["Nome"]}: '))
    # partidas.append(partidas_jogadas)
    for i in range(0, partidas_jogadas):
        gols_partida.append(int(input(f'Quantidade de gols feitos na partida {i+1}: ')))
    aproveitamento['gols'] = gols_partida.copy()
    aproveitamento['gols_total'] = sum(gols_partida)
    gols_partida.clear()
    jogadores.append(aproveitamento.copy())
    continuar = input('Quer continuar? [S/N] ').strip().upper()[0]
    if continuar == 'N':
        break

# formatacao = max(partidas)
print('=-'*50)
print(f'{"cod":^3} {"nome":<15} {"gols":<15} {"total":<5}')
print('-'*50)
max_len = 0
for cod, jogador in enumerate(jogadores):
    if cod == 0:
        max_len = len(jogador['gols'])
    elif len(jogador['gols'])>max_len:
        max_len = len(jogador['gols'])
    
for cod, jogador in enumerate(jogadores):
     print(f'{cod:>3} {jogador['Nome']:<15} {str(jogador['gols']):<15} {jogador['gols_total']}')
# print('=-'*25)

# print(f'O jogador {aproveitamento['Nome']} jogou {len(aproveitamento['gols'])} partidas.')
# for pos, val in enumerate(aproveitamento['gols']):
#     print(f'=> Na partida {pos+1}, fez {val} gols.')
# print(f'Fez um total de {aproveitamento['gols_total']} gols.')
# print('=-'*25)
     
while True:
    print('=-'*25)
    entrada = int(input('Mostrar dados de qual jogador: '))
    if entrada == 999:
        print('<< VOLTE SEMPRE >>')
        break
    elif entrada >= len(jogadores):
        print(f'ERRO! Não existe jogador com código {entrada}! Tente novamente')
        continue
    print(f'Levatamento do jogador {jogadores[entrada]['Nome']}')
    for partida, gols in enumerate(jogadores[entrada]['gols']):
        print(f'No jogo {partida} fez {gols} gols.')