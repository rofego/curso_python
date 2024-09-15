from pathlib import Path
import json
# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
def listar(lista):
    print('-'*10)
    for tarefa in lista:
        print(tarefa)
    print('-'*10)
    print()

def adicionar(elemento,caminho_arquivo,tarefas_lista=None):
    if tarefas_lista is None:
        tarefas_lista = []
    tarefas_lista.append(elemento)
    listar(tarefas_lista)
    salvar(tarefas_lista,caminho_arquivo)
    return

def desfazer(tarefas_lista, caminho_arquivo, tarefas_hist):
    if not tarefas_lista:
        print("NENHUM ELEMENTO PARA DESFAZER!")
        return
    tarefa = tarefas_lista.pop()
    tarefas_hist.append(tarefa)
    listar(tarefas_lista)
    salvar(tarefas_lista,caminho_arquivo)
    return

def refazer(tarefas_lista, caminho_arquivo, tarefas_hist):
    if not tarefas_hist:
        print("Completamente REFEITO!")
        return
    tarefa = tarefas_hist.pop()
    tarefas_lista.append(tarefa)
    listar(tarefas_lista)
    salvar(tarefas_lista,caminho_arquivo)
    return

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo,'r',encoding='utf8') as arquivo:
            json.load(tarefas,arquivo,ensure_ascii=False)
    except FileNotFoundError:
        print('Arquivo não existe.')
    return dados

def salvar(tarefas, caminho_arquivo):
    with open(caminho_arquivo, 'w',encoding='utf8') as arquivo:
        json.dump(tarefas,arquivo,ensure_ascii=False)

tarefas = []
tarefas_historico = []

CAMINHO_ARQUIVO = str(Path(__file__).parent)
CAMINHO_ARQUIVO+='\\tarefas.json'


    
while True:
    print()
    print('Desfazer, Refazer ou Adicionar(Basta digitar a tarefa)')
    tarefa = input('Digite a tarefa ou comando:')
    comandos = {
    'desfazer': lambda: desfazer(tarefas,CAMINHO_ARQUIVO,tarefas_historico),
    'refazer': lambda: refazer(tarefas, CAMINHO_ARQUIVO, tarefas_historico),
    'adicionar':lambda: adicionar(tarefa, CAMINHO_ARQUIVO, tarefas)
    }
    comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
    comandos.get('adicionar')
    comando()
# import os


# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()


# tarefas = []
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     if tarefa == 'listar':
#         listar(tarefas)
#         continue
#     elif tarefa == 'desfazer':
#         desfazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'refazer':
#         refazer(tarefas, tarefas_refazer)
#         listar(tarefas)
#         continue
#     elif tarefa == 'clear':
#         os.system('clear')
#         continue
#     else:
#         adicionar(tarefa, tarefas)
#         listar(tarefas)
#         continue