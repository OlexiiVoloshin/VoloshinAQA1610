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

    def test_filter_by_price(self):
        # Встановлення мінімальної та максимальної ціни
        min_price = 15000  # Встановіть бажану мінімальну ціну
        max_price = 30000  # Встановіть бажану максимальну ціну

        # Максимізація вікна браузера
        self.driver.maximize_window()
        # Знаходження та клік на вкладці "Ноутбуки і комп'ютери"
        notebooks_and_computers_tab = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-main-page/div/aside/rz-main-page-sidebar/div[1]/rz-sidebar-fat-menu/div/ul/li[1]",
        )
        notebooks_and_computers_tab.click()
        # Затримка на 2 секунд для демонстрації
        time.sleep(2)

        # Знаходження ноутбуків в  категорії
        first_category = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-super-portal/div/main/section/div[2]/rz-dynamic-widgets/rz-widget-list[1]/section/ul/li[1]/rz-list-tile/div",
        )
        first_category.click()
        # Затримка на 2 секунд для демонстрації
        time.sleep(2)

        # Введення мінімальної ціни
        min_price_input = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/aside/rz-filter-stack/div[4]/div/rz-scrollbar/div/div[1]/div/div/rz-filter-slider/form/fieldset/div/input[1]",
        )
        min_price_input.clear()
        min_price_input.send_keys(str(min_price))
        # Затримка на 5 секунд для демонстрації
        time.sleep(5)

        # Введення максимальної ціни
        max_price_input = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/aside/rz-filter-stack/div[4]/div/rz-scrollbar/div/div[1]/div/div/rz-filter-slider/form/fieldset/div/input[2]",
        )
        max_price_input.clear()
        max_price_input.send_keys(str(max_price))
        # Затримка на 5 секунд для демонстрації
        time.sleep(5)

        # Клік на кнопці "Застосувати"
        apply_button = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-category/div/main/rz-catalog/div/div/aside/rz-filter-stack/div[4]/div/rz-scrollbar/div/div[1]/div/div/rz-filter-slider/form/fieldset/div/button",
        )
        apply_button.click()
        # Затримка на 5 секунд для демонстрації
        time.sleep(5)

        # Перевірка, чи виведені продукти потрапляють у вказаний діапазон цін
        product_prices = self.driver.find_elements(By.XPATH, '//span[@class="price"]')
        for price_element in product_prices:
            product_price = int(price_element.text.replace("₴", "").replace(",", ""))
            self.assertTrue(min_price <= product_price <= max_price)


if __name__ == "__main__":
    unittest.main()
