class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None


    @property
    def motor(self):
        return self._motor

    @motor.setter
    def motor(self, motor_classe):
        self._motor = motor_classe

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, fabricante_nome):
        self._fabricante = fabricante_nome

class Motor:
    def __init__(self, nome):
        self.nome = nome
    


class Fabricante:
    def __init__(self, nome):
        self.nome = nome
        self.carros = []

    def inserir_carro(self, *carros):
        self.carros += carros

carro1 = Carro('Ford Ka')
motor1 = Motor('1.0, V8')
motor2 = Motor('1.6, V16')

carro1.motor = motor1

carro2 = Carro('Fiat Palio')
carro3 = Carro('Peugeot 208')

carro2.motor = motor1
carro3.motor = motor2

fabrica1 = Fabricante('Fiat')
fabrica2 = Fabricante('Ford/Peugeot')

carro1.fabricante = fabrica2
carro2.fabricante = fabrica1
carro3.fabricante = fabrica2


print(carro1.nome, carro1._motor.nome, carro1.fabricante.nome)
print(carro2.nome, carro2._motor.nome, carro2.fabricante.nome)
print(carro3.nome, carro3._motor.nome, carro3.fabricante.nome)