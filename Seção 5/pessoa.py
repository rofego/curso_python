class Pessoa:
    def __init__(self, nome: str) -> None:
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


class Cliente(Pessoa):
    def __init__(self, nome: str, cc=None, cp=None):
        super().__init__(nome)
        self.contacorrente = cc
        self.contapoupanca = cp
