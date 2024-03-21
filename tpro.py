import requests
from bs4 import BeautifulSoup

url = "https://tpro.by/products/khranenie_i_transportirovka/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

#data = soup.find("div", id="catalog")
data = soup.find("div", attrs={"id": "catalog"})
items = data.find("div", class_="item product sku")

#for i in items:
name = items.find("div" class_="productColText").text
    #price = i.find.all("a", class_="price").text

print(name)
    #print(price)

#bx_1762928987_20187 > div > div.productTable > div.productColImage > a > img