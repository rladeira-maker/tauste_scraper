''' Cria DIRECTORYetório para armazenar os dados e apaga qualquer arquivo
.csv'''
import os
import glob


def deleteFile(DIRECTORY, delete_file=True):
    '''
    Cria o diretório de trabalho se ele não exister - apaga todos csv 
    '''
    if (os.path.exists(DIRECTORY)) is not True:
        os.mkdir(DIRECTORY)
    if delete_file is True:
        for csv_file in glob.glob(DIRECTORY+"*.csv"):
            os.remove(csv_file)
    
