# Funções recursivas e recursividade
# - funções que podem se chamar de volta
# - úteis p/ dividir problemas grandes em partes menores
# Toda função recursiva deve ter:
# - Um problema que possa ser dividido em partes menores
# - Um caso recursivo que resolve o pequeno problema
# - Um caso base que para a recursão
# - fatorial - n! = 5! = 5 * 4 * 3 * 2 * 1 = 120
# https://brasilescola.uol.com.br/matematica/fatorial.htm
import sys
sys.setrecursionlimit(1002)
def recursiva(inicio=0, fim=10):
    # Caso recursivo
    # Contar até chegar ao final
    x = inicio
    if x >= fim:
        return x
    x+=1
    return recursiva(x, fim)

x = recursiva(0,1000)

print(x)