import time
from homework_21.pages.language_change_page import LanguageChangePage


def test_language_change(driver):
    base_url = "https://makeup.com.ua/ua/"
    time.sleep(3)
    driver.get(base_url)

    language_page = LanguageChangePage(driver)
    language_page.navigate_to_men_section()
    ua_header_text = language_page.get_header_text()
    time.sleep(3)
    language_page.change_language_to_ru()
    ru_header_text = language_page.get_header_text()
    time.sleep(3)
    assert (
        ua_header_text != ru_header_text
    ), "Текст заголовка не змінився після зміни мови"
