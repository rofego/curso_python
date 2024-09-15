from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem
    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self) -> bool:
        print('Email: enviando mensagem', self.mensagem)
        return True

class NotificacaoSMS(Notificacao):
    def enviar(self) -> bool:
        print('SMS: enviando mensagem', self.mensagem)
        return True

def notificar(notificacao: Notificacao):
    x = notificacao.enviar()
    if x:
        print('Notificação enviada!')
    else:
        print('Notificação não enviada!!')

sms = NotificacaoSMS("mensagem nova")
email = NotificacaoEmail('Nyt')

notificar(sms)
notificar(email)

# x = NotificacaoSMS('oi!')
# x.enviar()
