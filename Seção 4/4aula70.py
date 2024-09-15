'''
RETURN
'''

# def soma(x, y):
#     print('Oi')
#     return x + y

# soma1 = soma(2, 5)

# def mult(*args):
#     total = 1
#     for numero in args:
#         total *= numero
#     return total

# fat5 = mult(1,2,3,4,5)
# print(fat5)

def par_impar(x):
    if x%2==0:
        return 'par'.upper()
    return 'ímpar'.upper()

entrada = int(input('Digite um número: '))
par_ou_impar = par_impar(entrada)
print(par_ou_impar)
