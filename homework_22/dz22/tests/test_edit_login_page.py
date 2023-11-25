import random
import string
from homework_22.dz22.pages.edit_login_page import EditLoginPage


def generate_random_string(length):
    return "".join(random.choices(string.ascii_letters, k=length))


def test_edit_login(driver, base_url, login_credentials):
    new_name = generate_random_string(6)
    new_surname = generate_random_string(8)

    driver.get(base_url)
    edit_page = EditLoginPage(driver)

    edit_page.login_and_navigate(
        login_credentials["username"], login_credentials["password"]
    )
    edit_page.edit_name_and_surname(new_name, new_surname)
    assert (
        edit_page.is_popup_visible_and_close()
    ), "Спливаюче вікно не відображається після редагування профілю"
