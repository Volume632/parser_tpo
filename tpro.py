import requests
from bs4 import BeautifulSoup

url = "https://tpro.by/products/organayzer_qbrick_system_pro_organizer_200_mfi_red_ultra_hd_orgqpro200fczepg001/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

name = soup.find("div", class_="cheaper-product-name").text

price = soup.find(class_="priceVal").text

url_amg = data.find(class_="pictureSlider").get("picture")

print(url_amg)