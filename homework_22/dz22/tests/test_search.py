import time
from homework_22.dz22.pages.search_page import SearchPage


def test_search_for_product(driver):
    # Ініціалізуємо сторінку пошуку
    search_page = SearchPage(driver)

    # Перейдемо на головну сторінку сайту
    driver.get("https://makeup.com.ua/ua/")

    # Активуємо пошук
    search_page.activate_search()
    time.sleep(3)
    # Введемо "парфуми" та натиснемо Enter
    search_page.search("парфуми")
    time.sleep(3)
    # Перевіримо, чи ми перейшли на сторінку з результатами пошуку
    assert (
        "https://makeup.com.ua/ua/search/?q=%D0%BF%D0%B0%D1%80%D1%84%D1%83%D0%BC%D0%B8"
        in driver.current_url
    )
