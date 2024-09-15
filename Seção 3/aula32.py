"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# nmr = input('Digite um número inteiro: ')
# nmr_int = None
# par_impar = None
# if nmr.isdigit():
#     nmr_int = int(nmr)
#     par_impar = nmr_int % 2 == 0
#     if par_impar:
#         print(f'{nmr_int} é par.')
#     else:
#         print(f'{nmr_int} é ímpar.')
# else:
#     print(f'{nmr} não é inteiro')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são em numeros inteiros? ')
try:
    hora_int = int(hora)
    if hora_int >= 0 and hora_int <= 11:
        print('Bom dia!')
    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde!')
    elif hora_int >= 18 and hora_int <=23:
        print('Boa noite!')
    else:
        print('Essa hora não existe!')
except:
    print("Digite apenas números inteiros.")

# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
# menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
# "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
# """

# nome = input('Nome: ')
# nome_len = len(nome)
# if nome_len < 5:
#     print('Seu nome é curto')
# elif nome_len>=5 and nome_len<=6:
#     print('Seu nome é normal')
# else:
#     print('Seu nome é muito grande!')
