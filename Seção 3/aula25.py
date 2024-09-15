'''
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (0123456789ABCDEF)
'''
nome = 'Luiz'
preco = 1000.945345
variavel = '%s, o preço é R$%.2f'  %(nome, preco)
print(variavel) 
print('O hexadecimal de %d é %04X' % (16, 16))