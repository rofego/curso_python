# try, except, else, finally

try:
    print('ABRIR ARQUIVO')
    a = 9
    b = int(input())
    c = a/b

except ZeroDivisionError as e:
    print('Dividiu por zero')
    print(e)
    print(e.__class__.__name__)
else:
    print('Não deu erro.')
finally:
    print('FECHAR ARQUIVO')