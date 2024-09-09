from composicao import Cliente, Endereco


c1 = Cliente("Diego Nunes", 68)
c1.insere_endereco("Av da Pampulha",89,"Belo Horizonte","MG")
print(c1.nome)
c1.lista_endereco()
print()

c2 = Cliente("Maria Antônia", 52)
c2.insere_endereco("Rua Chile",74,"Salvador","BA")
c2.insere_endereco("Av Presidente Vargas",1,"Rio de Janeiro","RJ")
print(c2.nome)
c2.lista_endereco()
print()

c3 = Cliente("João Pedro", 39)
c3.insere_endereco("Higienópolis",1786,"São Paulo","SP")
print(c3.nome)
c3.lista_endereco()
print()