'''POO em Python - Associação

Associação: quando um atributo da classe recebe uma outra classe

Com isso, esse atributo da classe consegue executar métodos e chamar atributos da classe
que recebe. Contudo, nenhuma das duas é depende uma da outra, de modo que podem ser separadas uma
da outra.
Relação fraca entre duas classes.'''

class Escritor:
    def __init__(self, nome):
        self.__nome = nome
        self.__ferramenta = None

    @property
    def nome(self):
        return self.__nome
    
    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta
    
class Caneta:
    def __init__(self, marca):
        self.__marca = marca

    @property
    def marca(self):
        return self.__marca
    
    def escrever(self):
        print('Caneta está escrevendo...')


    
class MaquinaDeEscrever:
    def escrever(self):
        print('Máquina está escrevendo...')