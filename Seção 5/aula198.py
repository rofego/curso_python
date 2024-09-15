#class - são moldes para criar novos objetos.
# As classes geram novos objetos(instâncias) que
#podem ter seus próprios atributos e métodos(tem funções dentro
# da classe string que executam ações nos dados)
'''
string = 'Romulo' #str
print(string.upper())
print(isinstance(string,str))
'''
#Os objetos gerados pela classe podem usar seus dados 
#internos para realizar várias ações.

#Por convenção, usamos PascalCase para nomes de classe
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Luiz','Otávio') #inicializa uma classe
# p1.nome = 'Luiz'
# p1.sobrenome = 'Otávio'
# p2 = Pessoa()
# p2.nome = 'Santos'
# p2.sobrenome = 'Oliveria'
# print(p1)
# print(p1.nome)
# print(p1.sobrenome)
# print(p2)
# print(p2.nome)
# print(p2.sobrenome)

print(p1.nome)
print(p1.sobrenome)
