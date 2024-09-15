#Métodos em instâncias de classes Python
# class lista:
#     def __init__(self):
#         x = [1,3,2,7]
#         ...
#     def maior(x):
#         x = [1,3,2,7]
#         for i in range(3):
#             for j in range(3):
#                 var = x[j]
#                 if x[j]>x[j+1]:
#                     x[j] = x[j+1]
#                     x[j+1] = var
#         return x
    
# lista_1 = lista()
# print(lista_1.maior())

# class Carro:
#     def __init__(zzz, nome):
#         zzz.nome = nome
#     def acelerar(zzz):
#         print(f'{zzz.nome} está acelerando.')
    
# fusca = Carro('Fusca')
# print(fusca.nome)

# celta = Carro(nome='Celta')
# print(celta.nome)

# fusca.acelerar()

linha = list()
linha.append(2)
linha.append(3)
list.append(linha, 8)
print(linha)