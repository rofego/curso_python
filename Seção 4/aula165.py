# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.

def criar_funcao(funcao):
    def interna(*args, **kwargs):
        for arg in args:
            is_string(arg)
        resultado = funcao(*args,**kwargs)
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    print(inverte_string.__name__)
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('Precisa ser string')


hoje = inverte_string('123')
print(hoje)