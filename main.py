from bs4 import BeautifulSoup

# Загрузка HTML-файла
with open('example.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Создание объекта BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Поиск всех продуктов
products = soup.find_all('div', class_='product')

# Обработка каждого продукта
for product in products:
    # Извлечение названия продукта
    title = product.find('h3').text

    # Извлечение цены продукта
    price = product.find('span', class_='price').text

    # Извлечение описания продукта
    description = product.find('p').text

    # Проверка наличия и извлечение информации о скидке
    discount_tag = product.find('div', class_='discount')
    discount = discount_tag.text if discount_tag else 'No discount'

    # Вывод информации о продукте
    print(f"Title: {title}, Price: {price}, Discount: {discount}")