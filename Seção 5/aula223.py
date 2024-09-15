# Herança Múltipla - Python Orientado a Objetos
# Quer dizer que no Python, uma classe pode estender
# várias outras classes.
# Herança siples:
# Animal -> Mamífero -> Humano -> Pessoa -> Cliente
# Log -> FileLog
# Cliente(Pessoa, FileLog)
#
# 

class Animal:
    def __init__(self):
        print(f"Sou um animal")
    
class Mamifero(Animal):
    def __init__(self):
        print("Sou um mamífero.")
        super().__init__()

class Humano(Mamifero):
    def __init__(self):
        print(f'Sou um humano.')
        super().__init__()

class Pessoa(Humano):
    def __init__(self):
        print(f'Sou uma pessoa.')        
        super().__init__()
    
class Cliente(Pessoa):
    def __init__(self, nome):
        self.nome = nome
        print(f'Sou o cliente {self.nome}')
        super().__init__()

c1 = Cliente('Jorge Brandão')