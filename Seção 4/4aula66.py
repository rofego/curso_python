"""
Introdução às funções (def) em Python
Funções são trechos de código usados para 
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) 
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# def mostra_pra_mim(x='Vazio'):
#     for i in range(len(x),0,-1):
#         print(x[0:i])

# x = input()
# mostra_pra_mim(x)



"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""

# def soma(x ,y , z=0):#Se eu não coloco z=0, interpretador não aceita somente dois argumentos qnd uso a função
#     if z is not None: 
#         print(f'{x=} {y=} {z=}', x+y+z)
#     else:
#         print(f'{x=} {y=}', x+y)

# soma(1, 2)
# soma(3, 5)
# soma(100, 200)
# soma(7, 9, 0)

"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""
x = 1

def escopo():
    x = 10

    def outra_funcao():
        x=11
        y = 2
        print(x, y)
    
    outra_funcao()
    print(x)

print(x)
escopo()
print(x)

