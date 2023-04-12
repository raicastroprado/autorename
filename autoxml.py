
#codigo para colocar .xml no final de todos os arquivos  ou entao qualquer outro tipo de extensão seja XML, JPEG, PNG, TXT e etc.
import os

#sempre que colocar o caminho usar // na separação 
caminho_diretorio = ' coloque aqui o caminha desejado ' # caminho onde esta os arquivos para alterar lero lero
for nome_arquivo in os.listdir(caminho_diretorio):
    if not nome_arquivo.endswith('.xml'):
        novo_nome_arquivo = nome_arquivo + '.xml'
        os.rename(os.path.join(caminho_diretorio, nome_arquivo), os.path.join(caminho_diretorio, novo_nome_arquivo))
