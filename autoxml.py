
#codigo para colocar .xml no final de todos os arquivos  ou entao qualquer outro tipo de extensão seja XML, JPEG, PNG, TXT e etc.
import os

caminho_diretorio = 'C:\\Users\\Fiscal4\\Desktop\\XML SABÓ 06.01.23 A 22.01.23' # caminho onde esta os arquivos para alterar lero lero
for nome_arquivo in os.listdir(caminho_diretorio):
    if not nome_arquivo.endswith('.xml'):
        novo_nome_arquivo = nome_arquivo + '.xml'
        os.rename(os.path.join(caminho_diretorio, nome_arquivo), os.path.join(caminho_diretorio, novo_nome_arquivo))
