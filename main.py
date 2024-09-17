from scraping.jumia import products_jumia
from scraping.spacenet import products_spacenet
from tools import   menu
from data_base.select import len_site
from data_base.insert import update_dataBase
import json 
from tools import loading


_scraping=False 
_update_database=False

def main():
    global _scraping
    global _update_database
    x=menu()
    while x!=0 :

        match x :
            case 0 : return 
            case 1 :
                jumia = loading('Start scraping in site jumia',products_jumia)
                spacenet= loading('Start scraping in spacenet',products_spacenet)
                data={
                    'jumia':jumia,
                    'spacenet':spacenet
                }
                with open("data.json", "w") as f:
                    json.dump(data, f)
                _scraping=True
                _update_database=False
                print('\nYour data has been updated.\n')
            case 2: 
                if not _scraping :
                    print('\nYou need to start scraping before updating the database.\n')
                elif _update_database :
                    print('\nYour database is already updated.\n')
                else :
                    res=loading('Start update your database',update_dataBase)
                    _update_database=True
                    print('\nYour data base has been updated.\n')
            case 3 :
                if len_site == 0:
                    print('Your database is empty. scraping data then insert into the database to see the dashboard.')
                    
                
        x=menu()
            

            



main()