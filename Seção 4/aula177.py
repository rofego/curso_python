# filter é um filtro funcional

from aula176 import print_iter, produtos

print_iter(produtos)

def filtrar_preco(produto):
    return produto['preco'] > 100

# novos_produtos = [p for p in produtos if p['preco'] > 1000]
# list comprehesion com filter
novos_produtos = filter(#lambda p: p['preco']>100 
    filtrar_preco, produtos)

print_iter(novos_produtos)

# map -> pode alterar os dados, mesmo tamanho do iterável
# filtar -> ou o mesmo tamanho ou menos
# programação funcional -> função filter