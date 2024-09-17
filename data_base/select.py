from data_base.connect import connect


mydb=connect()
mycursor = mydb.cursor()
sql_len_site="select count(id) from site"
sql_len_category="select count(id) from category"
sql_len_product="select count(id) from product"

def len_site():
    mycursor.execute(sql_len_site)
    res = mycursor.fetchall()
    return res[0][0]

def len_category():
    mycursor.execute(sql_len_category)
    res = mycursor.fetchall()
    return res[0][0]

def len_product():
    mycursor.execute(sql_len_product)
    res = mycursor.fetchall()
    return res[0][0] 




