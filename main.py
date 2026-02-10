import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Настройка драйвера Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Открытие локальной HTML-страницы
    driver.get("file:///path/to/your/local/form_page.html")  # Укажите путь к вашей локальной HTML-странице

    # Поиск полей формы
    name_input = driver.find_element(By.NAME, "name")
    email_input = driver.find_element(By.NAME, "email")
    submit_button = driver.find_element(By.NAME, "submit")

    # Заполнение формы
    name_input.send_keys("Ваше имя")
    email_input.send_keys("example@example.com")

    # Имитирование нажатия кнопки "Submit"
    submit_button.click()

    # Небольшая задержка, чтобы увидеть результат
    time.sleep(2)

finally:
    # Закрытие браузера
    driver.quit()