import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}
for count in range(1, 14):

    sleep(3)
    url = f"https://antamedia.by/elektronika/elektroinstrumenty/perforatory/?page={count}"

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", attrs={"class": "row-flex row-price category-page"})
    items = data.find_all("div", class_="product-layout")

    for i in items:
        name = i.find("div", class_="product-name").text
        url_amg = i.find("img").get("src")
        price = i.find("div", class_="price").text

        print(name, price, url_amg)