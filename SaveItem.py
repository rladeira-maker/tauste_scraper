''' Salva o arquivo .csv desejado. Recebe o diretório, o nome do arquivo
e a lista que será salva linha a linha '''
import csv


def saveItem(list_input, name, DIRECTORY):
    '''salva os arquivos na past de trabalho'''
    try:
        with open(DIRECTORY+name+".csv", "a") as fopen:  # Open the csv file.
            csv_writer = csv.writer(fopen)
            csv_writer.writerow(list_input)
            return True
    except:
        return False
