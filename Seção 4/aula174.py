from itertools import combinations, permutations, product
def print_iter(iterator):
    print(*list(iterator),sep='\n')
    print()

pessoas = [ 'João','Joana','Luiz','Letícia']

camisetas = [['preta','branca'],['p','m'],]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))