from bs4 import BeautifulSoup
import requests


#get tous les categori ------------------- 
def get_category():
    doc = requests.get("https://www.jumia.com.tn/catalog/")
    soup = BeautifulSoup(doc.content, 'html.parser')
    category_links = soup.find_all('a', {'data-eventaction': 'category'})
    category = []
    for link in category_links:
        name = link['href'].split("/")[1]
        category.append(name)
    return category

#['ordinateurs-accessoires-informatique', 'electronique', 'sports-loisirs', 'terrasse-jardin-exterieur',
#  'telephone-tablette', 'jeux-et-jouets', 'fashion-mode', 'animalerie', 'maison-cuisine-jardin',
#  'epicerie', 'automobile-outils', 'beaute-hygiene-sante', 'bebe-puericulture', 'livres-papeterie']



def products_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = []
        all = soup.find_all('article', {'class': 'prd _fb col c-prd'})
        for i in all:
            product = {}
            product['name'] = i.find('h3').text.strip()
            old_price_div = i.find('div', {"class": "old"})
            if old_price_div:
                product['prix_o'] = old_price_div.text.strip().split(" ")[0]
            else:
                product['prix_o'] ='0'  
 
            product['prix_r'] = i.find('div', {"class": "prc"}).text.strip().split(" ")[0] 
            product['img'] = i.find('img')['data-src']
            product['lien'] = "https://www.jumia.com.tn/" + i.find('a', {'class': 'core'})['href']
            product['note'] = i.find('div', {"class": "stars _s"})
            if product['note'] is not None:
                product['note'] = product['note'].text.strip().split(" ")[0]
            else:
                product['note'] = None
            products.append(product)
        
        return products
    except requests.exceptions.RequestException:
        return []


def products_jumia():
    products_data = {}
    category=get_category()
    for i in category:
        page = 1
        category_products = []

        while True:
            page_url = f"https://www.jumia.com.tn/{i}/?&price_discount=10-100&page={page}"
            products_page = products_info(page_url)

            if products_page: 
                category_products+= products_page 
                
            else :
                break 
            page += 1
            
        products_data[i] = category_products
    return products_data
        
        


