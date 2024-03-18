import requests
from bs4 import BeautifulSoup

#for count in range(1, 14):
url = "https://antamedia.by/elektronika/elektroinstrumenty/perforatory/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")
data = soup.find_all("div", attrs={"class": "row-flex row-price category-page"})

for i in data:
    name = i.find("div", class_="product-name").text
    url_amg = i.find("img").get("src")
    price = i.find("div", class_="price").text

print(name + price + url_amg)