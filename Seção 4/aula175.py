# # groupby - agrupando valores (itertools)
# from itertools import groupby

# alunos = [
#     {'nome': 'Luiz', 'nota': 'A'},
#     {'nome': 'Letícia', 'nota': 'B'},
#     {'nome': 'Fabrício', 'nota': 'A'},
#     {'nome': 'Rosemary', 'nota': 'C'},
#     {'nome': 'Joana', 'nota': 'D'},
#     {'nome': 'João', 'nota': 'A'},
#     {'nome': 'Eduardo', 'nota': 'B'},
#     {'nome': 'André', 'nota': 'A'},
#     {'nome': 'Anderson', 'nota': 'C'},
# ]

# alunos_ordenados = sorted(alunos, key=lambda x:x['nota'])
# grupos = groupby(alunos_ordenados, key=lambda x:x['nota'])

# for chave, aluno in grupos:
#     print(chave)
#     for a in aluno:
#         print(list(aluno))