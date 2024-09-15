from aula176 import produtos
from functools import reduce
# reduce - faza a redução de um iterável em um valor

# total = 0
# for p in produtos:
#     total += p['preco']

# print(total)

# x = [p['preco'] for p in produtos]
# print(sum(x))
# print(sum(x))
def funcao_do_reduce(total, produto):
    return total + produto['preco']

total = reduce(funcao_do_reduce, produtos,0)

print(total)