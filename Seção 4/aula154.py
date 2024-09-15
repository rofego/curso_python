# Entendendo os seus próprios módulos Python
# O primeiro módulo executando chama-se __main__
# Você pode importar outro módulo inteiro ou parte do módulo
# O python conhece a pasta onde o __main__ está
# e as pastas abaixo dele
# Ele não reconhece pastas e módulos acima do __main__ por padrão
# O python conhece todos os módulos e pacotes presentes
# nos caminhos sys.path
import aula154_m
import sys
print('Esse módulo chama-se', __name__)
print(*sys.path, sep='\n')