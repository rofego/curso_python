# Variaveis livres + Nonlocal (locals, globals)
# def fora(x):
#     a = x
#     # Variável livre -> a
#     # Variável livre: não está definida dentro do escopo da função 'dentro'
#     # Free Vars
#     def dentro():
#         # print(locals())
#         print(dentro.__code__.co_freevars)
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(20)
# print(dentro1(), dentro2())

def concatenar(string):
    valor_final = string
    def interna(valor_concat=''):
        nonlocal valor_final
        valor_final+=valor_concat
        return valor_final
    return interna

c = concatenar('Oi')
c('x')
c('x')
c('x')
c('x')
final = c()
print(final)