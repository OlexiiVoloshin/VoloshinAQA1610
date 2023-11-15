import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RozetkaUATests(unittest.TestCase):
    def setUp(self):
        # Ініціалізація драйвера Chrome
        self.driver = webdriver.Chrome()
        # Відкриття головної сторінки
        self.driver.get("https://rozetka.com.ua/ua/")

    def tearDown(self):
        # Завершення роботи драйвера після кожного тесту
        self.driver.quit()

    def test_click_on_cart_icon(self):
        # Максимізація вікна браузера
        self.driver.maximize_window()

        # Знаходження та клік на іконці кошика
        cart_icon = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[7]",
        )
        cart_icon.click()
        # Затримка на 5 секунд для демонстрації
        time.sleep(5)
        # Очікування відображення поп-апу після натискання кошика
        popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/app-root/rz-single-modal-window")
            )
        )

        # Перевірка, чи поп-ап дійсно відображений
        self.assertTrue(popup.is_displayed())


if __name__ == "__main__":
    unittest.main()
