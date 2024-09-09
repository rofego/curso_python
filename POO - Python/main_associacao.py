from associacao import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('Geraldo')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()

escritor.ferramenta = caneta
escritor.ferramenta.escrever()
print(escritor.ferramenta.marca)