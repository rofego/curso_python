'''
try except
'''
numero_str = input(
    'Vou dobrar o número que vc digitar: '
)

try:
    print("STRING:", numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float*2:.2f}')
except:
    print("Isso não é um número")

