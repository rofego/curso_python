# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        print(f'{self.nome} está filmando.')
        self.filmando = True

c1 = Camera('tekpix')
c1.filmar()
c1.filmar()
c1.filmar()
c1.filmar()
c1.filmar()

