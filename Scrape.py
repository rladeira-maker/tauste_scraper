'''Retira os dados de cada "card" existente na página web- identificação
 do produto (product_id), nome do produto (title) e o preço praticado
  (price)'''
from WriteToCsv import write_to_csv


def scrape(source_url, soup):
    '''Takes the driver and the subdomain for concats as params'''
    # Find the elements of the products
    cards = soup.find_all('li',class_='item product product-item')
    fileName = (str(source_url).rpartition('/')[-1]).replace('.html', '').rsplit(sep='?')[0]

    # Iterate over each product tag
    for item in cards:
        title = item.find_all("a",class_='product-item-link')[1].get_text().strip().replace('&amp;', 'e')  #aqui pego o nome do produto
        products_prices = (item.find_all("span",class_='price-wrapper'))
        idx = 0
        while (products_prices[idx].get('data-price-type')) == 'oldPrice':
            idx = idx + 1
        price = (products_prices[idx].get_text().split()[1].replace(',','.'))
        product_id = item.find_all('div', class_='price-box')[0].get('data-product-id')
        splited_title = title.split(' ')
        price_per_kilo = ''
        price_per_litre = ''
        
        '''Extrai o peso/volume e calcula o valor do preço por litro ou quilo'''
        for item in splited_title:
            if item.upper().find('KG')>0 and item.upper().split('KG')[0].isnumeric():
                weight = float((item.upper().split('KG')[0]).replace(',','.'))
                price = price.replace(',','.')
                price_per_kilo = (str(round((float(price)/weight)*1 , 2)))#.replace('.', ',')
            if item.upper().find('G')>0 and item.upper().split('G')[0].isnumeric():
                weight = float((item.upper().split('G')[0]).replace(',','.'))
                price = price.replace(',','.')
                price_per_kilo = (str(round((float(price)/weight)*1000, 2)))#.replace('.', ',')
            if item.upper().find('L')>0 and item.upper().split('L')[0].isnumeric():
                volume = float((item.upper().split('L')[0]).replace(',','.'))
                price = price.replace(',','.')
                price_per_litre = (str(round((float(price)/volume)*1 , 2)))#.replace('.', ',')
            if item.upper().find('ML')>0 and item.upper().split('ML')[0].isnumeric():
                volume = float((item.upper().split('ML')[0]).replace(',','.'))
                price = price.replace(',','.')
                price_per_litre = (str(round((float(price)/volume)*1000, 2)))#.replace('.', ',')
        
        write_to_csv([product_id, title, price, '', price_per_kilo, price_per_litre, fileName.upper(),'Tauste'])

