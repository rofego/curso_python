# Encapsulamento (modificadores de acesso: public, protected, private)
# Pyhton NÃO TEM modificadores de acesso
# Mas podemos seeguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qlqr lugar
#   _(um underline) = protected
#       NÃO DEVE ser usado fora da classe
#   __(dois underlines) = private
#       "name manling" (dessfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só deve ser usado na classe em que foi declarado.
from functools import partial

class Fools:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
