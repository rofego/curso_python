pessoa = {}

chave = 'name'
pessoa[chave] = 'Rômulo'

print(pessoa[chave])

pessoa['sobrenome'] = 'Fialho'

print(pessoa)

del pessoa['sobrenome']

print(pessoa)

print(pessoa.get('surname', False))

