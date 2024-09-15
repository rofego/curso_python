# '''
# CÁLCULO DO PRIMEIRO DÍGITO VERIFICADOR
# CPF: 345.789.067-98
# Colete a soma  dos 9 primeiros digitos do cpf
# multiplicando cada um  dos valores por uma contagem regressiva
# começando de 
# EX.: 10 9 8 7 6 5 4 3 2 
#      3  4 5 7 8 9 0 6 7 

#      somar todos os resultados
#      multilpicar esse reultado por 10
#      Obter o resto da divisão anterior por 11
# Se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resultado é o valor da conta

# O primeiro dígito do CPF é 7
# '''
# import re
# cpf = input('Digite CPF: ')
# # cpf = cpf.replace('.','').replace(' ','').replace('-','')
# cpf = re.sub(r'[^0-9]','',cpf)
# primeiro_caract = cpf[0]
# primeiro_caract *= len(cpf)
# if primeiro_caract==cpf:
#     print('CPF inválido. Dados sequenciais.')
#     quit()
# nove_digitos = cpf[:-2]
# resultado = 0
# mult = 10
# for digito in nove_digitos:
#     resultado += mult* int(digito)
#     mult -= 1


# resultado *= 10

# digito_1 = 0
# digito_1 = 0 if resultado%11>9 else resultado%11
# print('-='*30)
# print(f'O primeiro dígito verificador(após o traço) é {digito_1}')
# print('-='*30)
# '''
# CÁLCULO DO SEGUNDO DÍGITO VERIFICADOR
# colete a soma dos 10 primeiros dígitos
# multiplicando cada um dos valores por uma contagem regressiva começando de 11
# soma todos os resultados
# multplica por 10
# Obtem o resultado da divisão por 11
# se o resultado anterior for maior que 9:
#     resultado é 0
# contrário disso:
#     resutlado é o valor da conta

# '''
# dez_digitos = cpf[:-1]
# mult_2 = 11
# resultado_2 = 0
# for digito in dez_digitos:
#     resultado_2 += mult_2*int(digito)
#     mult_2-=1
# resultado_2 *=10
# digito_2 = 0 if resultado_2%11>9 else resultado_2%11
# print(f'O segundo dígito verificador(após o traço) é {digito_2}')

# cpf_gerado = f'{nove_digitos}{digito_1}{digito_2}'

# if cpf == cpf_gerado:
#     print(f'{cpf} é um CPF válido.')
# else:
#     print('CPF inválido.')

import random

cpf_aleat_9 = ''
for i in range(0,9):
    cpf_aleat_9 += f'{random.randint(0,9)}'


resultado_1 = 0
mult = 10
for digito in cpf_aleat_9:
    resultado_1 += mult*int(digito)
    mult -= 1
resultado_1 *= 10
digito_1 = 0 if resultado_1%11>9 else resultado_1%11
cpf_aleat_10 = f'{cpf_aleat_9}{digito_1}'
resultado_2=0
mult_2 = 11
for digito in cpf_aleat_10:
    resultado_2 += mult_2*int(digito)
    mult_2 -=1
resultado_2*=10
digito_2 = 0 if resultado_2%11>9 else resultado_2%11
cpf_aleat_valido=f'{cpf_aleat_10}{digito_2}'
print(f'CPF gerado: {cpf_aleat_valido}')