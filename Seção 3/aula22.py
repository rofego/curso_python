# entrada = input('[E]ntrar e [S]air: ')
# senha_digitada = input('Senha: ')

# senha_perm = '123456'

# if (entrada=='E' or entrada=='e') and senha_digitada==senha_perm:
#     print('Entrar')
# else:
#     print('Sair')

#AVALIAÇÃO DE CURTO CIRCUITO
print(False or 0 or '123' or True)

senha = input('Senha: ') or 'Sem senha'
print(senha)