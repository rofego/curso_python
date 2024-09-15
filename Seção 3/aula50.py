"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Ana','Tiago','Pedro']
indices = len(lista)
for i in range(0,indices):
    print(f'{lista[i]} [{i}]')