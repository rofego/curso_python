# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro

# pessoa = {
#     'alunos': ['Pedro', 'Caio'], 
#     'notas':[7,8],
#     }

# # print(list(pessoa.items()))

# for chave in pessoa.keys():
#     print(chave)
#     for valor in pessoa[chave]:
#         print(valor)

import copy
d1 = {
    'c1':1,
    'c2':2,
    'lista':[1,2,3],
}

d2 = copy.deepcopy(d1)
d2['lista'].append(4)
print(d1,d2)

nmr = d2.popitem('c1')
print(nmr)