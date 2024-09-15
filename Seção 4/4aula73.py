'''
Higher Order Functions
First Class Functions
Funções de primeira classe
'''

# def saudacao(msg, nome):
#     return f'{msg}, {nome}'

# def executa(funcao, *args):
#     return funcao(*args)
# saudacao_2 = executa(saudacao, 'Bom dia','Ana')
# print(saudacao_2)

'''
Closure e funções que retornam outras funções 
'''

# def criar_saudacao(saudacao):
#     def saudar(nome):
#         return f'{saudacao}, {nome}!'
#     return saudar

# falar_bom_dia = criar_saudacao("Bom dia")
# falar_boa_noite = criar_saudacao("Boa noite")

# print(falar_bom_dia("Ana"))
# print(falar_boa_noite("Clara"))

'''
Exercícios
Crie funções que duplicam, triplicam e quadruplicam
o número recebido como parâmetro
'''

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return multiplicador*numero
    return multiplicar


lista =['dobro', 'triplo','quádruplo']
for i in range(2,5):
    dobro = criar_multiplicador(i)
    z = dobro(int(input()))
    print(lista[i-2],'=',z)