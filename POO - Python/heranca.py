'''POO em Python - Herança

Herança é a relação mais íntima entre classes dentre as 4. 
É quando a classe é outra. 

Num pequeno resumo:
Associação - usa
Agregação - Tem
Composição - É dono
Herança - É'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeclasse} Falando...')

class Cliente(Pessoa):
    pass

class Aluno(Pessoa):
    pass