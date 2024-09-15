'''
Operação Ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
'''
nmr = int(input('Digite um nmr: '))
str_condicao = 'Par' if nmr%2==0 else 'Ímpar'
print(str_condicao)