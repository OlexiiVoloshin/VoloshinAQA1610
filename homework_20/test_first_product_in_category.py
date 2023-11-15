import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class RozetkaUATests(unittest.TestCase):
    def setUp(self):
        # Ініціалізація драйвера Chrome
        self.driver = webdriver.Chrome()
        # Відкриття головної сторінки
        self.driver.get("https://rozetka.com.ua/ua/")

    def tearDown(self):
        # Завершення роботи драйвера після кожного тесту
        self.driver.quit()

    def test_click_on_first_product_in_category(self):
        # Максимізація вікна браузера
        self.driver.maximize_window()

        # Знаходження та клік на вкладці "Ноутбуки і комп'ютери"
        notebooks_and_computers_tab = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[1]/rz-sidebar-fat-menu/div/ul/li[1]",
        )
        notebooks_and_computers_tab.click()
        # Затримка на 2 секунди для демонстрації
        time.sleep(2)

        # Знаходження ноутбуків в категорії
        first_category = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-list[1]/section/ul/li[1]/rz-list-tile/div/a[2]",
        )
        first_category.click()
        # Затримка на 2 секунди для демонстрації
        time.sleep(2)

        # Перевірка, чи коректно перейшли на сторінку з ноутбуками
        expected_url = "https://rozetka.com.ua/ua/notebooks/c80004/"
        current_url = self.driver.current_url
        self.assertEqual(expected_url, current_url)

if __name__ == "__main__":
    unittest.main()
