
#faforlife product knowledge base
from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://faforlife.com/product.php').text
soup = BeautifulSoup(html_text, 'lxml')
products = soup.find_all('div', class_ = 'col-lg-4 col-md-6')

for index, product in enumerate (products):
    details = []
    product_name = product.find('h3', class_ = 'tp-project-title-3').text
    details.append(product_name)

    product_details = soup.find_all('h3', class_ = 'tp-project-details-subtitle')
    for detail in product_details:
        details.append(detail.text)                    
    product_detail = ' | '.join(str(x) for x in details)

    link = 'https://faforlife.com/'
    product_page = product.find('h3', class_ = 'tp-project-title-3').a['href']
    link += product_page

    product_description = requests.get(link).text
    soup = BeautifulSoup(product_description, 'lxml')
    descriptions = soup.find_all('div', class_ = 'container')

    uses = []
    for description in descriptions:
        product_uses = description.find_all('p', class_ = 'tp-project-details-list-title mb-3')
        for use in product_uses:
            uses.append(use.text)          
    use = ', '.join(str(x) for x in uses)

    print(f'''
    Product Name: {product_detail}
    Product Uses: {use}
    Product Link: {link}
    ''')

    with open(f'KnowledgeBase.txt', 'a') as f:
        f.write(f"Product Name: {product_detail.strip()}\n")
        f.write(f"Product Uses: {use.strip()}\n")
        f.write(f"Product Link: {link.strip()}\n")
        f.write('-' * 40 + '\n\n')
    print(f'Product added to KnowledgeBase.txt: {index}')
