# Exercício - Salve sua classe JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos.
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'Seção 5\\pessoa.json'
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa("Joao", 33)
p2 = Pessoa("Joana", 56)
p3 = Pessoa("Carlos", 43)
bd = [vars(p1), vars(p2), vars(p3)]

with open(CAMINHO_ARQUIVO,'w') as arquivo:
    json.dump(bd, arquivo, ensure_ascii=False, indent=2)