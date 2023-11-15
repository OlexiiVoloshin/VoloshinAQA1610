import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class RozetkaUATests(unittest.TestCase):
    def setUp(self):
        # Ініціалізація драйвера Chrome
        self.driver = webdriver.Chrome()
        # Відкриття головної сторінки
        self.driver.get("https://rozetka.com.ua/ua/")

    def tearDown(self):
        # Завершення роботи драйвера після кожного тесту
        self.driver.quit()

    def test_input_text_in_search_box(self):
        # Максимізація вікна браузера
        self.driver.maximize_window()

        # Знаходження поле пошуку та введення тексту
        search_box = self.driver.find_element(By.NAME, "search")
        search_box.send_keys("смартфони samsung")
        search_box.send_keys(Keys.ENTER)
        # Затримка на 5 секунд для демонстрації
        time.sleep(5)

        # Перевірка, чи знайдений текст з'явився на сторінці
        self.assertTrue("смартфони samsung" in self.driver.page_source.lower())


if __name__ == "__main__":
    unittest.main()
