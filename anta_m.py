import requests
from bs4 import BeautifulSoup

url = "https://antamedia.by/elektronika/elektroinstrumenty/perforatory/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find("div", attrs={"id": "content"})
items = data.find("div", class_="row-flex row-price category-page")
#items = data.find_all("div", attrs={"class":"product-layout"})
#content > div.row-flex.row-price.category-page > div:nth-child(1)

name = data.find("div", class_="product-name").text

price = soup.find(class_="price_no_format").text

url_amg = data.find("img").get("src")

print(name + "\n" + price + "\n" + url_amg + "\n\n")