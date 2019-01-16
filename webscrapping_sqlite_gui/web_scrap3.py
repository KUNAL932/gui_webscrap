
from bs4 import BeautifulSoup
import requests
import pandas as pd

book_name_list=[]
book_price_list=[]
avail_stock=[]
book_id = []
book_dict={}

website_name="http://books.toscrape.com/"
result=requests.get(website_name,verify=False)

soup=BeautifulSoup(result.text,"html.parser")
books=soup.findAll("article",{"class":"product_pod"})
i = 1
for book in books:
    name=book.findAll("a")[1].attrs['title']
    book_name_list.append(name)

    price=book.find("p",{"class":"price_color"}).text[2:]
    price = price.strip()
    book_price_list.append(price)

    stock = book.find("p",{"class":"instock availability"}).text
    stock = stock.strip()
    avail_stock.append(stock)

    book_id.append(i)
    i=i+1

book_dict["book name"]=book_name_list
book_dict["book price"]=book_price_list
book_dict["availability"]=avail_stock
book_dict['BOOK_ID'] = book_id

to_show=pd.DataFrame(data=book_dict)
to_show=to_show.set_index('BOOK_ID')
print(to_show.head())
print(to_show)
to_show.to_csv("book.csv")

