# @property + @setter

class Caneta:
    def __init__(self, cor):
        self._cor = cor
    
    @property
    def cor(self):
        return self._cor

    @cor.setter
    def cor(self, cor):
        self._cor = cor
    
caneta = Caneta('Roxo')
caneta.cor = 'Azul'
print(caneta.cor)