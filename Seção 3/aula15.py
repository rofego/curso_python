entrada = input('1 ou 0?')
entrada_int = int(entrada)

if entrada_int==1:
    print(f'Você escolheu {entrada_int} e ficará no sistema')
elif entrada_int==0:
    print(f'Você escolheu {entrada_int} e sairá do sistema')
else:
    print(f'Você é burro?')
