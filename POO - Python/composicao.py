'''POO em Python - Composição

Composição: qunado uma classe está contida na outra

A vida do objeto contido depende da vida do objeto que o contém.
Se ese último for apagado, o objeto contido também é deletado.
Por isso, é um relação entre duas classes considerada forte.'''

class Cliente:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
        self.enderecos = []

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        self._idade = idade
    
    def insere_endereco(self, rua, numero, cidade, estado):
        self.enderecos.append(Endereco(rua, numero, cidade, estado))

    def lista_endereco(self):
        for endereco in self.enderecos:
            print(f'{endereco.rua}, {endereco.numero} - {endereco.cidade}, {endereco.estado}')


class Endereco:
    def __init__(self, rua, numero, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.cidade = cidade
        self.estado = estado
    
