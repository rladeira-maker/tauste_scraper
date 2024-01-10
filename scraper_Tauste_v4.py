'''Main file'''
import datetime as dt
from DeleteFile import deleteFile
from BrowseAndScrape import browse_and_scrape


def main(pages,delete_file):
    '''main file - loads pages list and scrape web pages'''
    DIRECTORY = '../Mercado'
    DIRECTORY = DIRECTORY + '_' + dt.datetime.now().date().isoformat() + '/'
    try:
        deleteFile(DIRECTORY, delete_file)
    except:
        print('parece que ocorreu um erro')
    for page in pages:
        SEED_URL = "https://tauste.com.br/saojosedoscampos"+page
        print("\nWeb scraping has begun")
        result = browse_and_scrape(SEED_URL)
        if result is True:
            pass
        else:
            print(f"Oops, That doesn't seem right!!! - {result}\n")
    if result is True:
        print("Web scraping is now complete!")
    else:
        print(f"Oops, That doesn't seem right!!! - {result}\n")
