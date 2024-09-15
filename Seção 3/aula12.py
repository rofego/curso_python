print('Nome:', end=' ')
nome = str(input())

print('Altura:', end=' ')
altura = float(input())

print('Peso:', end=' ')
peso = float(input())

imc = peso/altura**2

#formatação de strings: exmplo de um tipo - f-string
linha_1 = f'{nome} tem {altura:.2f} m e {peso:.1f} kg e IMC: {imc:.2f}'
print(linha_1)

#formatação de strings: format
#obs.: as variaveis em python sáo objetos
#por isso, tem métodos(pode fazer ações)
linha_1 = '{} tem {:.2f} m, {:.1f} kg e IMC: {:.2f}'
formato = linha_1.format(nome, altura, peso, imc)
print(formato)  


