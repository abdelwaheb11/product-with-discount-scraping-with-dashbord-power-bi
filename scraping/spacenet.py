from bs4 import BeautifulSoup
import requests , re


#get tous les categori -------------------
def get_category():
    text="fourniture-bureautique-tunisie,electromenager-tunisie,gamer-pc-ps4-tunisie,informatique,maison-brico,meuble-de-jardin-maison,securite-reseaux,telephonie,image-son"
    category=text.split(',') 
    return category

def products_info(url):
    try:
        response = requests.get(url)
        response.raise_for_status() 
        soup = BeautifulSoup(response.content, 'html.parser')
        
        products = []
        all = soup.find_all('div',{'class': 'field-product-item item-inner product-miniature js-product-miniature'})
        for i in all:
            product = {}
            h2=i.find('h2')
            product['name'] = h2.text.strip()
            product['prix_o'] =re.sub(r'[^\d,.]', '', i.find('span', {"class": "regular-price"}).text.strip().split(" ")[0])
            product['prix_r'] =re.sub(r'[^\d,.]', '', i.find('span', {"class": "price"}).text.strip().split(" ")[0])
            product['img'] = i.find('span',{'class' : 'cover_image'}).find('img')['src']
            product['lien'] = h2.find('a')['href']
            product['note'] = None
            products.append(product)
        
        return products
    except requests.exceptions.RequestException:
        return []



def products_spacenet():
    category=get_category()
    products_data = {}
    for i in category:
        page = 1 
        category_products = []
        while True:
            page_url = f"https://spacenet.tn/promotions?categories={i}&page={page}"
            products_page = products_info(page_url)
            if category_products and products_page[-1]['name'] == category_products[-1]['name'] :
                break
            else :
                category_products+= products_page
                
            #products_data[i] = category_products
            page += 1
        products_data[i] = category_products
    return products_data
        
        


