"""
Iterando strings com while
"""
#       012345678910
nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
# print(nome)
# print(tamanho_nome)
# print(nome[3])

nome_string = ''
contador = 0
while contador < tamanho_nome:
    letra = nome[contador]
    nome_string += f'*{letra}' 
    contador += 1
nome_string += '*'
print(nome_string)
