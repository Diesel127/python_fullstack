from selenium import webdriver
import time

# Создаем экземпляр драйвера браузера
driver = webdriver.Chrome()

# Открытие первой страницы в новой вкладке
driver.get('https://www.example.com')
# Задержка для загрузки страницы
time.sleep(2)

# Открытие второй страницы в новой вкладке
driver.execute_script("window.open('');")
driver.switch_to.window(driver.window_handles[1])
driver.get('https://www.example.org')
# Задержка для загрузки страницы
time.sleep(2)

# Переключение обратно на первую вкладку
driver.switch_to.window(driver.window_handles[0])
# Задержка для демонстрации переключения
time.sleep(2)

# Переключение снова на вторую вкладку
driver.switch_to.window(driver.window_handles[1])
# Задержка для демонстрации переключения
time.sleep(2)

# Закрытие всех вкладок и завершение работы браузера
driver.quit()
