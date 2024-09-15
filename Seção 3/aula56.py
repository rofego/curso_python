"""
split e join com list e str
split - divide uma string (list) -MÉTODO
join - une uma string
"""
frase = "          Eu fui na feira,    mas não comprei arroz."
lista_palavras_cruas = frase.split(',')
lista_palavras = []
for pos, val in enumerate(lista_palavras_cruas):
    lista_palavras.append(val.strip())
print(lista_palavras)
frases_unidas = '333'.join(lista_palavras)
print(frases_unidas)