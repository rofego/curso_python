# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açúcar sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        resultado = func(*args, **kwargs)
        return resultado
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]

invertida = inverte_string('123')
print(invertida)