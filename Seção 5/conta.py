from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float = 0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abstractmethod
    def sacar(self, valor: float):
        pass

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'(DEPÓSITO{valor})')

    def detalhes(self, msg=''):
        print(f'Saldo: {self.saldo} - Conta: {self.conta} - \
              AG:{self.agencia}', msg)


class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int,
                 saldo: float = 0, limite: float = 0):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor, banco):
        novo_valor = self.saldo - valor
        limite = self._limite + self.saldo
        if valor > limite:
            self.detalhes(f'(SAQUE DE {valor} NEGADO POR EXCEDER O SALDO \
                           {self.saldo} MAIS O LIMITE DE {self._limite} )')
            return
        if banco.autenticar:
            self.saldo = novo_valor
            self.detalhes(f'(SAQUE {valor})')
        else:
            self.detalhes(f'(SAQUE NEGADO {valor})')


class ContaPoupanca(Conta):
    def __init__(self, agencia, conta, saldo):
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
