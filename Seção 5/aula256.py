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
import conta
import pessoa
import banco
cc1 = conta.ContaCorrente(12, 34567, 4, 100)
cc2 = conta.ContaCorrente(12, 34567)
cp1 = conta.ContaPoupanca(11, 15342, 900)
c1 = pessoa.Cliente('Pedro', cc1, cp1)
c2 = pessoa.Cliente("Mara", None, conta.ContaPoupanca(12, 12343, 589))
c3 = pessoa.Cliente("Ferdinando", conta.ContaCorrente(
    1, 22222, 9000, 3000), None)

nubank = banco.Banco()
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
