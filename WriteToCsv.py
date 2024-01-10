'''Serve unicamente para criar a primeira linha caso o arquivo ainda não
tenha sido criado. Talvez possa ser juntado com o saveItem'''
import datetime as dt
import os
from SaveItem import saveItem


def write_to_csv(list_input, name='allGroceries', DIRECTORY='../Mercado'):
    '''The scraped info will be written to a CSV here.'''
    DIRECTORY = DIRECTORY + '_' + dt.datetime.now().date().isoformat() + '/'

    if (os.path.isfile(DIRECTORY+name+'.csv')) is not True:
        saveItem(['ID', 'PRODUTO', 'PRECO-FINAL', 'PRECO-CHEIO', 'PRECO/KG', 'PRECO/L', 'SECAO', 'MERCADO'], name, DIRECTORY)
        saveItem(list_input, name, DIRECTORY)
    else:
        saveItem(list_input, name, DIRECTORY)
