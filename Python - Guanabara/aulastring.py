'''
Manipulando Textos
'''

# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
# G o s t o   m u i t  o     d  e     v  o  c  ê
# nome = 'Gosto muito de você'

# print(f'nome: {nome[::]}.')
# print(f'{random.sample(nome,5)}')
# print(f'nome: {nome[::]}.')
# print(nome.find('itos')) # - 1 -> Não foi encontrado

# print('Gto' in nome)

# print(nome.replace('você','dela'))
# print(nome)
# print(nome.upper().find('MUITO'))
# print(nome)
# print(nome.lower())
# print(nome.capitalize())
# print(nome.title())
# frase_space = '    Aprenda Python  '
# print(frase_space.strip()) 
# #frase.rstrip() -> remove espaços da direita ou frase.lstrip() -> remove espaços da esquerda
# print(frase_space)
# #frase.split()
# print('''To be, or not to be, that is the question:
# Whether 'tis nobler in the mind to suffer
# The slings and arrows of outrageous fortune,
# Or to take arms against a sea of troubles
# And by opposing end them. To die—to sleep,
# No more; and by a sleep to say we end \n''')

'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas
- O nome com todas minúsculas
- Quantas letras ao todo(sem considerar espaços)
- Quantas letras tem o primeiro nome
'''
# nome_completo = input('Digite seu nome completo: ').strip()

# print(f'Nome com todas as letras maiúsculas: {nome_completo.upper()}')

# print(f'Nome com todas as letras minúsculas: {nome_completo.lower()}')

# nome_no_space = nome_completo.replace(' ','')

# print(f'Seu nome tem {len(nome_no_space)} letras.')

# nomes_split = nome_completo.split()

# print(f'O primeiro nome tem {len(nomes_split[0])} letras.')

'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
Ex.: Digite um número: 1234
'''
# numero_string = input('Digite o número: ').rjust(4,'0')

# print(f'Unidade: {numero_string[3]}')
# print(f'Dezena: {numero_string[2]}')
# print(f'Centena: {numero_string[1]}')
# print(f'Milhar: {numero_string[0]}')

# numero = int(input('Digite um número: '))

# milhar = numero//1000
# centena = (numero-(milhar*1000))//100
# dezena = (numero-(milhar*1000+centena*100))//10
# unidade = (numero-(milhar*1000+centena*100+dezena*10))//1
# print(f'Unidade: {unidade}')
# print(f'Dezena: {dezena}')
# print(f'Centena: {centena}')
# print(f'Unidade de Milhar: {milhar}')

'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome 'santo'
'''
# cidade = input('Digite o nome da cidade: ').strip()
# if cidade.upper().find('SANTO')==0:
#     print(f'{cidade} começa com "Santo"') 
# else:
#     print(f'{cidade} não começa com "Santo".')

'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome
'''
# nome_completo = input('Digite seu nome completo: ').strip().upper()
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m',
#          'pretoebranco':'\033[7;30m',
#          'boldazulverm':'\033[1;36;41m',
#          'boldverdbran':'\033[1;32;40m',
#          'boldbranverd':'\033[1;30;42m',
#          'noneverdpret':'\033[7;32m'}
# if 'SILVA' in nome_completo:
#     print(f'O(A) Sr(a) {cores['boldazulverm']} {nome_completo} {cores['limpa']} tem "Silva" no nome.')
# else:
#     print(f'O(A) Sr(a) {cores['boldazulverm']} {nome_completo} {cores['limpa']} não tem "Silva" no nome.')

'''
Faça um programa que leia uma frase pelo teclado e mostre:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece pela primeira vez
- Em que posição ela aparece pela última vez
'''
# frase = input('Frase: ').strip()
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m',
#          'pretoebranco':'\033[7;30m',
#          'boldazulverm':'\033[1;36;41m',
#          'boldverdbran':'\033[1;32;40m',
#          'boldbranverd':'\033[1;30;42m',
#          'noneverdpret':'\033[7;32m'}
# cont = 0
# print(f'A letra "A" aparece {cores["boldbranverd"]} {frase.upper().count('A')} {cores["limpa"]} vezes')
# print(f'A letra "A" aparece pela primeira vez no índice {cores["boldverdbran"]} {frase.upper().find('A')} {cores["limpa"]}')
# # for pos, letra in enumerate(frase):
# #     if letra in 'Aa':
# #         cont +=1
# #     if letra in 'Aa' and cont == frase.upper().count('A'):
# #         print(f'A letra "A" aparece pela última vez no índice {pos}')
# print(f'A letra "A" aparece pela primeira vez no índice {frase.upper().rfind('A')}')

'''
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último
nome separadamente
'''
# nome_completo = input('Digite seu nome completo: ').strip().upper()
# nome_split = nome_completo.split(' ')

# print(f'Prenome: {nome_split[0]}\nÚltimo nome: {nome_split[-1]}')

    
