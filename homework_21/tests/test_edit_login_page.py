import time
import random
import string
from homework_21.pages.edit_login_page import EditLoginPage


def generate_random_string(length):
    return "".join(random.choice(string.ascii_letters) for _ in range(length))


def test_edit_login(driver):
    base_url = "https://makeup.com.ua/ua/"
    username = "runyellowjack@gmail.com"
    password = "Vtusya23"
    new_name = generate_random_string(6)
    new_surname = generate_random_string(8)

    driver.get(base_url)
    edit_page = EditLoginPage(driver)

    edit_page.login(username, password)
    time.sleep(3)
    edit_page.navigate_to_account()
    time.sleep(3)
    edit_page.edit_name_and_surname(new_name, new_surname)
    assert edit_page.is_popup_visible(), "Спливаюче вікно підтвердження не відображається"
    edit_page.close_popup()
