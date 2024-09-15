import json

from aula207_a import CAMINHO_ARQUIVO, Pessoa

with open(CAMINHO_ARQUIVO,'r') as arquivo:
    pessoas = json.load(arquivo)
    lista_de_pessoas = []
    for pessoa in pessoas:
        x = Pessoa(**pessoa)
        lista_de_pessoas.append(x)
for pessoa in lista_de_pessoas:
    print(pessoa.nome, pessoa.idade)