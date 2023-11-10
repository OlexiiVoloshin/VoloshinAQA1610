import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

    def test_click_on_login_button(self):
        # Максимізація вікна браузера
        self.driver.maximize_window()

        # Знаходження та клік на кнопці входу
        login_button = self.driver.find_element(
            By.XPATH,
            "/html/body/app-root/div/div/rz-header/rz-main-header/header/div/div/ul/li[3]",
        )
        login_button.click()

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
