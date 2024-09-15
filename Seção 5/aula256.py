"""Exercício com Abstração, Herança, Encapsulamento e Polimorfismo

Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta(ABC)
    ContaCorrente
    ContaPoupanca

Pessoa(ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe cliente que herda por herança da classe Pessoa 
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta(Agregação da classe ContaCorrente ou ContaPoupança)


"""
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia:int, conta:int, saldo:float=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
   
    @abstractmethod
    def sacar(self, valor:float):
        pass

    def depositar(self, valor):
        self.saldo+=valor
        self.detalhes(f'(DEPÓSITO{valor})')
    
    def detalhes(self, msg=''):
        print(f'Saldo: {self.saldo} - Conta: {self.conta} - AG:{self.agencia}',msg)
    


class ContaCorrente(Conta):
    def __init__(self, agencia:int, conta:int, saldo:float=0,limite:float=0):
        super().__init__(agencia, conta, saldo)
        self._limite = limite
    
    def sacar(self, valor,banco):
        novo_valor = self.saldo - valor
        limite = self._limite + self.saldo
        if valor > limite:
            self.detalhes(f'(SAQUE DE {valor} NEGADO POR EXCEDER O SALDO {self.saldo} MAIS O LIMITE DE {self._limite} )')
            return
        if banco.autenticar:
            self.saldo = novo_valor
            self.detalhes(f'(SAQUE {valor})')
        else:
            self.detalhes(f'(SAQUE NEGADO {valor})')

class ContaPoupanca(Conta):
    def __init__(self,agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    def sacar(self, valor, banco):
        novo_valor = self.saldo - valor
        if novo_valor < 0:
            self.detalhes(f'(SAQUE NEGADO {valor})')
            return
        if banco.autenticar:
            self.saldo = novo_valor
            self.detalhes(f'(SAQUE {valor})')
        else:
            print("CLIENTE NÂO CORRETAMENTE CADASTRADO OU INEXISTENTE")
            self.detalhes(f'(SAQUE NEGADO {valor})')

class Pessoa:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

class Cliente(  Pessoa ):
    
    def __init__(self, nome, cc=None, cp=None):
        self._nome = nome
        self.contacorrente = cc
        self.contapoupanca = cp


class Banco:
    def __init__(self):
        self.clientes = []
        # self.contas = []
        # self.agencias = []

    def adiciona_cliente(self, cliente):
        if cliente not in self.clientes:
            self.clientes.append(cliente)
        else:
            print('CLiente já cadastrado')
        # if cliente.nome not in self.clientes:
        #     self.clientes.append(cliente.nome)
        # if cliente.contacorrente != None and cliente.contacorrente not in self.contas:
        #     self.contas.append(cliente.contacorrente)
        # if cliente.poupanca != None and cliente.poupanca not in self.contas:
        #     self.contas.append(cliente.poupanca)
    
    def autenticar(self, cliente):
        if cliente in self.clientes:
            return True
        return False

cc1 = ContaCorrente(12, 34567, 4, 100)
cc2 = ContaCorrente()
cp1 = ContaPoupanca(11, 15342, 900)
c1 = Cliente('Pedro', cc1, cp1)
c2 = Cliente("Mara",None, ContaPoupanca(12, 12343, 589))
c3 = Cliente("Ferdinando", ContaCorrente(1, 22222, 9000, 3000), None)

nubank = Banco()
nubank.adiciona_cliente(c1)
nubank.adiciona_cliente(c2)
nubank.adiciona_cliente(c3)
input('Continua?')
nubank.adiciona_cliente(c2)
print()
# c1.contacorrente.sacar(300,nubank)
# c1.contapoupanca.sacar(300,nubank)
# # c2.contacorrente.depositar(200,nubank)
# # c2.contapoupanca.depositar(200,nubank)
# c3.contacorrente.sacar(2300, nubank)