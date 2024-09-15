# a,b = 1,2
# a,b = b,a

pessoa = {
    'nome':'Aline',
    'sobrenome':'Souza'
}

# (a,b),(c,d) = pessoa.items()
# print(a,b,c,d)

# for chave, valor in pessoa.items():
#     print(chave, valor)

dados_pessoa = {
    'idade':16, 'altura':1.6
}

pessoas_completa = {**pessoa, **dados_pessoa}

# print(pessoas_completa)

# kwargs - keywords argumentos (argumentos nomeados)

def mostro_argumentos_nomeados(*args, **kwargs):
    print(f'Não nomeados => {args}')
    for chave, valor in kwargs.items():
        print(chave,'=', valor)

# mostro_argumentos_nomeados('R', 123, 'S',nome='Joana', qualquer_coisa=123)
mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1':1,
    'arg2':2,
    'arg3':3
}

mostro_argumentos_nomeados(**configuracoes)