primeiro_valor=input('Digite um valor: ')
segundo_valor=input('Digite outro valor: ')

int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)

if int_primeiro_valor>int_segundo_valor:
    linha_1 = f'{primeiro_valor=} é maior do que {segundo_valor=}'
    print(linha_1)
elif int_primeiro_valor<int_segundo_valor:
    linha_1 = f'{segundo_valor=} é maior do que {primeiro_valor=}'
    print(linha_1)
elif int_primeiro_valor==int_segundo_valor:
    linha_1 = f'{primeiro_valor=} é igual a {segundo_valor=}'
    print(linha_1)
else: 
    print('Erro')
