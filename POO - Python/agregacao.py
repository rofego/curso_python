'''POO em Python - Agregação

Agregaçâo: onde uma classe possui o objeto de outra

A vida do objeto agregado não depende da vida do objeto agregador
Se objeto agregador for deletado, o objeto agregado vai continaur existindo no programa
Por isso, é considerado uma relação fraca entre duas classes.'''

#classe que possui/agrega
class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def inserir_produto(self, produto):
        self.produtos.append(produto)

    def lista_produto(self):
        for produto in self.produtos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total+= produto.valor
        return total

#classe agregada
class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
