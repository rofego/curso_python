import aula156_m

print(aula156_m.variavel)

for i in range(10):
    import aula156_m

print('Fim')

# O import módulo é um singleton
# O import é para todo o programa sem a necessidade de importar novamente

import importlib

for i in range(10):
    importlib.reload(aula156_m)

# detalhe: o importlib.reload() implementa no programa alterações feitas no módulo