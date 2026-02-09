import unittest
from selenium import webdriver

class TestExampleDomain(unittest.TestCase):
    def setUp(self):
        # Создаем экземпляр драйвера браузера
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")

    def test_open_page(self):
        # Проверка заголовка страницы
        self.assertEqual(self.driver.title, "Example Domain")

    def tearDown(self):
        # Закрытие браузера после выполнения теста
        self.driver.quit()

unittest.main()
