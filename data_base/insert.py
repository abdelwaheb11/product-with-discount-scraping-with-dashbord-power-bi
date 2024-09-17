from data_base.connect import connect
from data_base.select import len_site
import json , time

mydb=connect() 
mycursor = mydb.cursor()
insert_site = "INSERT INTO site VALUES (null,%s)"
insert_product = "INSERT INTO product VALUES (null,%s, %s,%s, %s,%s, %s,%s,%s)"
insert_category = "INSERT INTO category VALUES (null,%s,%s)"

with open("data.json") as f: 
    data = json.load(f)

def get_prix(prix: str):
    if ',' in prix and '.' in prix:
        prix = prix.replace(',', '')
        return float(prix)
    elif ',' in prix:
        prix = prix.replace(',', '.')
        return float(prix)
    else: 
        return float(prix)

def prodcut_liste(products,ids,idc) : 
    ls=[]
    for p in products:
        note = float(p['note']) if p['note'] is not None else None
        prix_o=get_prix(p['prix_o'])
        prix_r=get_prix(p['prix_r'])
        product=(p['name'],prix_o,prix_r,note,p['img'],p['lien'],ids,idc)
        ls.append(product)
    return ls

def insert_data():
    for site, categorys in data.items():
        mycursor.execute(insert_site, (site,))
        id_s=mycursor.lastrowid
        mydb.commit()
        for category , products in categorys.items():
            mycursor.execute(insert_category, (category,id_s))
            id_c=mycursor.lastrowid
            mydb.commit()
            _products=prodcut_liste(products,id_s,id_c)
            for product in _products :
                mycursor.execute(insert_product,product)
            mydb.commit()


def clear_tables():
    mycursor.execute("delete from `site` ")
    mycursor.execute("ALTER TABLE site AUTO_INCREMENT = 1")
    mycursor.execute("ALTER TABLE category AUTO_INCREMENT = 1")
    mycursor.execute("ALTER TABLE product AUTO_INCREMENT = 1 ")
    mydb.commit() 
    
    

def update_dataBase():
    clear_tables()
    time.sleep(3)
    insert_data()
    return 

