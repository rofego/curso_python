# str_secret = 'Palavra Secreta'.lower()


# str_len = len(str_secret)
# str_attempt = ''
# attempts = 0
# teste = False


# print(f'{5*'-'}Adivinhe a palavra secreta{5*'-'}')


# while teste == False:
    
#     letra = input('Tente uma letra: ')
#     if attempts == 0 and letra in str_secret and letra not in str_attempt:
#         for i in range(0,str_len):
#             if letra == str_secret[i]:
#                 str_attempt += letra
#             else:
#                 str_attempt += ' '
#         print(f'Acertou mizeravi {str_attempt}')
#     elif letra in str_secret and letra not in str_attempt:
#         for i in range(0,str_len):
#             if letra == str_secret[i]:
#                 str_attempt= letra
#         print(f'Acertou mizeravi {str_attempt}')
#     elif letra in str_attempt:
#         print('Letra já digitada!')
#     else:
#         print('Mas tu é burro!?')
#     attempts += 1
#     if str_attempt == str_secret:
#         teste = True
#         print('Acaboooooooouu! Vai que é tua Brasil!')
# print("Fim do While")
# import os
# palavra_secreta = "Treinamento".lower()

# conj_de_letras_certas = ''
# palavra_formada = ''
# tentativas = 0


# print(f'{5*'-'}Adivinhe a palavra secreta{5*'-'}')
# while True:
    
#     letra = input('Tente uma letra: ')

#     if len(letra)>1:
#         print('Digite apenas uma letra.')
#         continue

#     if letra in palavra_secreta:
#         conj_de_letras_certas+=letra
#     palavra_formada=''
#     os.system('cls')
#     for i in palavra_secreta:
#         if i in conj_de_letras_certas:
#             palavra_formada += i
#         else:
#             palavra_formada += '*'
#     print(palavra_formada)
#     tentativas +=1
    
#     if palavra_formada == palavra_secreta:
#         break


# print(f'Parabens! Você achou a resposta em {tentativas} tentativas')

palavra = "Historia"
palavra_adivinhada = ""
letras_digitadas = ""
tentativas = 0
 
while True:
    letra = input("Digite uma letra da palavra secreta:  ").lower()
    tentativas += 1
 
    if len(letra) > 1:
        print("Escreva apenas uma letra!! \n")
        continue
 
    if letra in letras_digitadas:
        print("Já você digitou essa letra, digite outra: \n")
        continue
 
    if letra not in letras_digitadas:
        letras_digitadas += letra
 
    for i in palavra.lower():
        if i in letras_digitadas:
            palavra_adivinhada += i
        else:
            palavra_adivinhada += "*"     
 
    print(f"Palavra = {palavra_adivinhada}\n")
 
    if palavra_adivinhada == palavra.lower():
        print("Você ganhou, achou a palavra secreta!!")
        break
 
    if palavra != palavra_adivinhada:
        palavra_adivinhada = ""
    
    print(f"Você já usou {tentativas} tentativas \n") 