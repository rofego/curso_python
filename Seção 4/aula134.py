def executa(funcao, *args):
    return funcao(*args)

def soma(x,y):
    return x+y

def cria_multiplicador(multiplicador):
    def multiplica(numero):
        return numero * multiplicador
    return multiplica

duplica = cria_multiplicador(2)
print( executa(lambda x, y: x+y, 2,3), executa(soma, 2,3))
print(duplica(3))