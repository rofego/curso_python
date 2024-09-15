# Relações entre os objetos
# UML - link: https://en.wikipedia.org/wiki/Unified_Modeling_Language
# Associação, Agregação e Composição

# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_enderecos(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Maria')
cliente1.inserir_enderecos('Av Brasil', 54)
cliente1.inserir_enderecos('Av Presidente Vargas', 33)

cliente1.listar_enderecos()