# copy, sorted, produtos.sort
# Exercícios

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# Aumente os preços dos produtos a seguir em 10%

# Gere novos_produtos por deep copy (cópia profunda)
import copy
novos_produtos = [
    {**p, 'preco':round(p['preco']*1.1,2)}
    for p in copy.deepcopy(produtos)
]


# Ordene os produtos por nome decrescente (do maior para menor)
novos_produtos.sort(key= lambda item: item['preco'], reverse=True)
print(*novos_produtos, sep='\n')
print()
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(novos_produtos, key=lambda item: item['nome'] )
print(*produtos_ordenados_por_nome, sep='\n')

# Ordene os produtos por preco crescente (do menor para maior)
novos_produtos.sort(key= lambda item: item['preco'])

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = copy.deepcopy(novos_produtos)
produtos_ordenados_por_preco = sorted(produtos_ordenados_por_nome, key=lambda item: item['preco'])
