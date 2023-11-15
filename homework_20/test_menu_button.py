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

    def test_click_on_menu_button(self):
        # Максимізація вікна браузера
        self.driver.maximize_window()

        # Знаходження та клік на кнопці меню
        menu_button = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/rz-mobile-user-menu/button",
        )

        menu_button.click()
        # Затримка на 5 секунд для демонстрації
        time.sleep(5)

        # Очікування відображення поп-апу після натискання меню
        popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, "/html/body/div[3]/div[2]/div/nav")
            )
        )

        # Перевірка, чи поп-ап є видимим
        self.assertTrue(
            popup.is_displayed(), "Поп-ап не відображено після кліку на кнопку меню"
        )
if __name__ == "__main__":
    unittest.main()
