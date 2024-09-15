perguntas = [
    {
        'Pergunta':'Quanto é 2+2?',
        'Opções':['1','2','3','4','5'],
        'Resposta':'4',
    },
    {
        'Pergunta':'Quanto é 5*5?',
        'Opções':['25','55','100','22','50'],
        'Resposta':'25',
    },
    {
        'Pergunta':'Quanto é 10/2?',
        'Opções':['10','2','5','1','20'],
        'Resposta':'5',
    },
]
acertos = 0
for p in perguntas:
    print('Pergunta: ',p['Pergunta'],'\n')
    print('Opções:')

    for i, opcao in enumerate(p['Opções']):
        print(f'{i})',end=' ')
        print(opcao)
    resp = -1
    print()
    while True:
        resp = input("Escolha uma opção:")
        if resp.isdigit():
            resp = int(resp)
            if resp>=0 and resp<5:
                break
        else:
            print("Somente número inteiro entre 0 e 4.")
    if p['Opções'][resp] == p['Resposta']:
        acertos+=1
        print('Resposta certa:☻', p['Resposta'])
    else:
        print('Acertou!☻')
        print('Errroooou!')
        print('Resposta certa:', p['Resposta'])
    print(30*'-')

print("Jogo Encerrado.")
print("Total de acertos: %d de %d"%(acertos,len(perguntas))) 
print()
print(30*'-')