'''Extrai todas as páginas de um segmento (hortfrut, por exemplo) até a
última. Cada página é enviada para scrape.py (soup e url)'''
import time
import requests
from bs4 import BeautifulSoup
from Scrape import scrape


def browse_and_scrape(seed_url, page_number=1):
    # Fetch the URL - We will be using this to append to images and info routes
    source_url = seed_url

    # Page_number from the argument gets formatted in the URL & Fetched
    try:
        html_text = requests.get(source_url).text
        # Prepare the soup
        soup = BeautifulSoup(html_text, "html.parser")
        print(f"Now Scraping - {source_url}")

        # This if clause stops the script when it hits an empty page

        if soup.find("a", class_='action next') is not None:
            scrape(source_url, soup)     # Invoke the scrape function
            # Be a responsible citizen by waiting before you hit again
            time.sleep(3)
            # Recursively invoke the same function with the increment
            seed_url = soup.find("a", class_='action next').get('href')
            browse_and_scrape(seed_url, page_number)
        else:
            scrape(source_url, soup)     # The script exits here
            return True
        return True
    except Exception as e:
        return e
