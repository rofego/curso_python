from log import LogPrintMixin, LogFileMixin

class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False


    def desligar(self):
        if self._ligado:
            self._ligado = False
    

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            
class Smartphone(Eletronico, LogFileMixin):
    @property
    def ligado(self):
        return self._ligado

    def ligar(self):
        super().ligar()
        if self._ligado:
            msg = f'{self._nome} está ligado.'
            self.log_success(msg)

    def desligar(self):
        super().desligar()
        if not self._ligado:
            msg = f'{self._nome} está desligado.'
            self.log_error(msg)
