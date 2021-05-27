
from os import replace
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq

my_url = 'https://www.flipkart.com/mobiles/~cs-lc6ah0kamu/pr?sid=tyy%2C4io&collection-tab-name=Poco+X3+Pro&param=7883&otracker=clp_bannerads_1_15.bannerAdCard.BANNERADS_Poco%2Bx3%2Bpro_mobile-phones-store_X4GKU9R9Q9AF'

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, features="html.parser")  
containers = page_soup.find_all("div",{"class":"_2kHMtA"})
#container = containers[0] 


filename = "product1.csv"  
f = open(filename,"w")  
  
headers = "Product_Name,Pricing,Ratings\n"  
f.write(headers)  
#print(soup.prettify(container))
for container in containers:
    product_name = container.find_all("div",{"class":"_4rR01T"})
    product =product_name[0].text
    #print(product)
    price = container.find_all("div",{"class":"_30jeq3 _1_WHN1"})
    nprice = price[0].text.strip()
    #print(nprice)
    rating1 = container.find_all("div",{"class":"_3LWZlK"})
    rating = rating1[0].text
    #print(rating)


    edit_price = ''.join(nprice.split(',')) 
    sym_rupee = edit_price.split("?")  
    add_rs_price = "Rs"+sym_rupee[0]  
    split_price = add_rs_price.split("E")  
    final_price = split_price[0]  

    split_rating = str(rating).split(" ")
    final_rating = split_rating[0]

    #print(product.replace(",","|")+","+final_price+","+final_rating+"\n")

    f.write(product.replace(",","|")+","+final_price+","+final_rating+"\n")
f.close()