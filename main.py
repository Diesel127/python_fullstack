import urllib.request

# URL-адрес, с которого будем получать HTML-код
url = "https://example.com"

# Открываем URL и считываем HTML-код
with urllib.request.urlopen(url) as response:
    # Читаем содержимое страницы
    html_code = response.read()

# Декодируем HTML-код в строковый формат и выводим на экран
print(html_code.decode('utf-8'))