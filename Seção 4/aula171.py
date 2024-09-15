'''
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nvoa lista com os valores somados:

Se uma lista for maior que a outra, a soma só vai considerar o tamanho da menor.

Exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

*************** resultado
lista_soma = [2, 4, 6, 8]
'''
def soma(lista1, lista2):
    # intervalo = min(len(lista1), len(lista2))
    # resultado = [lista1[i]+lista2[i] for i in range(intervalo)]
    resultado = [x+y for x,y in zip(lista1, lista2)]
    return resultado
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

print(soma(lista_a,lista_b))