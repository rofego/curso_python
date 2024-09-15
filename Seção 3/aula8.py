print('Nome:',end=' ')
nome = str(input())

print('Sobrenome:',end=' ')
sobrenome = str(input())

print('Idade:',end=' ')
idade= int(input())

print('Ano de Nascimento:',end=' ')
ano_nascimento = int(input())

print('Altura em metros:',end=' ')
altura_metros = float(input())
print('\n')

maior_de_idade = idade >= 18
print('Nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de Nascimento:', ano_nascimento)
print('É maior de idade:', maior_de_idade)
print('Altura em metros:', altura_metros)