import requests
from bs4 import BeautifulSoup

url = "https://tpro.by/products/organayzer_qbrick_system_pro_organizer_200_mfi_red_ultra_hd_orgqpro200fczepg001/"

response = requests.get(url)

soup = BeautifulSoup(response.text, "lxml")

data = soup.find("div", class_="cheaper-product-name")
print(data)