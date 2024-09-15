from pathlib import Path

caminho_projeto = Path()
# print(caminho_projeto.absolute())

caminho_arquivo = Path.home() / "OneDrive" / "Área de Trabalho" / "arquivo.txt"
# print(caminho_arquivo.absolute())
# print()
# print(caminho_arquivo.parent)
# print()

ideias = caminho_arquivo.parent / 'ideias'
# print(ideias)

# arquivo = Path.home() / "OneDrive" / "Área de Trabalho" / "arquivo.txt"
# arquivo.touch()
# print(arquivo)
# arquivo.write_text('Show')
# print(arquivo.read_text())
# arquivo.unlink()

# with caminho_arquivo.open('+a') as file:
#     file.write('Uma linha\n')
#     file.write('Outra linha\n')

caminho_pasta = Path.home() / "OneDrive" / "Área de Trabalho" / "Python" 
caminho_pasta.rmdir()