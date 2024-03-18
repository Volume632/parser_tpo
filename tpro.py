import requests
from bs4 import BeautifulSoup

url = "https://tpro.by/products/khranenie_i_transportirovka/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find_all("div", id="catalogColumn")
for i in data:
    name = i.find("a", class_="name").text
    price = i.find(class_="priceVal").text
#url_amg = data.find("a", img="src").get

print(name + price)

#bx_1762928987_20187 > div > div.productTable > div.productColImage > a > img