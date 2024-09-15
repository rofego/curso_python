"""Calculadora com While"""
while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite o outro numero: ')
    operador = input('Digite o operador (+-/*): ')

    resultado = None
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        #má prática de programação imprimir 'error' ou usar except

    if numeros_validos is None:
        print('Um ou ambos dos numeros não são válidos: ')
        continue

    ###
    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue

    if len(operador)>1:
        print('Digite apenas um operador:')
        continue

    ###
    if operador == '+':
        resultado = num_1_float + num_2_float
        print(f'Resultado: {resultado}')
    elif operador == '-':
        resultado = num_1_float - num_2_float
        print(f'Resultado: {resultado}')
    elif operador == '/':
        resultado = num_1_float/num_2_float
        print(f'Resultado: {resultado}')
    elif operador == '*':
        resultado = num_1_float * num_2_float
        print(f'Resultado: {resultado}')
    else:
        print('Não deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    print(sair)
    if sair == True:
        break