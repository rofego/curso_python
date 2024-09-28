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
        # if cliente.contacorrente != None and cliente.contacorrente not in
        # self.contas:
        #     self.contas.append(cliente.contacorrente)
        # if cliente.poupanca != None and cliente.poupanca not in self.contas:
        #     self.contas.append(cliente.poupanca)

    def autenticar(self, cliente):
        if cliente in self.clientes:
            return True
        return False
