# Relações entre os objetos
# UML - link: https://en.wikipedia.org/wiki/Unified_Modeling_Language
# Associação, Agregação e Composição

# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.

# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramentas(self, ferramenta):
        self._ferramenta = ferramenta

class FerramentadeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo.'

escritor = Escritor('Luiz')
caneta = FerramentadeEscrever('Caneta Bic')
escritor._ferramenta = caneta

print(escritor.ferramenta.escrever())