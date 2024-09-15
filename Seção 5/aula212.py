# @property - um getter no modo Pythonico
# getter - um metodo para obter um atributo 
# cor -> get_cor()
# modo pyhtonico - modo do python de fazer coisas
# @property é uma propriedade do objeto, ela 
# é um método que se comporta como um
# atributo 
# Geralmente, é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        return self.cor_tinta

caneta = Caneta('azul')
print(caneta.cor)