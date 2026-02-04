from bs4 import BeautifulSoup
import csv

# Загрузка HTML-файла
with open('products.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Настройка CSS-селекторов для извлечения данных
product_selector = '.product'
name_selector = '.product-name'
price_selector = '.product-price'

# Извлечение данных
products = soup.select(product_selector)
product_data = []

for product in products:
    name = product.select_one(name_selector)
    price = product.select_one(price_selector)
    if name and price:
        name = name.get_text(strip=True)
        price = price.get_text(strip=True)

        product_data.append([name, price])
        print(f"Product: {name}, Price: {price}")
# Экспорт данных в CSV

with open("products.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Name", "Price"])
    writer.writerows(product_data)