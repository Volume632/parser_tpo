import requests
from bs4 import BeautifulSoup
import openpyxl
from time import sleep

headers = {"User-Agent":
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"}

# URL для парсинга
    
sleep(3)
url = "https://antamedia.by/elektronika/elektroinstrumenty/perforatory/?page="

def parse_page(url):
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    products = []
    
    # Поиск всех карточек продуктов
    data = soup.find("div", attrs={"class": "row-flex row-price category-page"})
    items = data.find_all("div", class_="product-layout")

    for i in items:
        title = i.find("div", class_="product-name").text.strip()
        price = i.find("div", {"class": "price"}).text.strip()
        url_amg = i.find("img").get("src")
    
        products.append({
        "Название": title,
        "Цена": price,
        "Ссылка на картинку": url_amg
        })
    
    return products
    

def write_to_excel(products):
    # Создание нового Excel-файла
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Перфораторы"
    
    # Заголовки столбцов
    headers = ['Название', 'Цена', 'Ссылка на картинку']
    for col_num, header in enumerate(headers, 1):
        col_letter = openpyxl.utils.get_column_letter(col_num)
        sheet[f"{col_letter}1"] = header
    
    # Заполнение данными
    for row_num, product in enumerate(products, 2):
        sheet[f"A{row_num}"] = product['Название']
        sheet[f"B{row_num}"] = product['Цена']
        sheet[f"C{row_num}"] = product['Ссылка на картинку']
    
    # Сохранение файла
        workbook.save(filename="products.xlsx")

if __name__ == "__main__":
    products = parse_page(url)
    write_to_excel(products)
    print("Данные успешно сохранены в файле products.xlsx")