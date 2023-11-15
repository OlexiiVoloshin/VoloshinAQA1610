import time
from homework_21.pages.login_page import LoginPage


def test_login_functionality(driver):
    base_url = "https://makeup.com.ua/ua/"
    username = "runyellowjack@gmail.com"
    password = "Vtusya23"

    driver.get(base_url)
    login_page = LoginPage(driver)

    login_page.login(username, password)
    time.sleep(3)

    login_page.navigate_to_account()

    actual_email = login_page.get_email_value()
    assert actual_email == username, (
        f"Електронна адреса на сторінці облікового запису не відповідає очікуваній. "
        f"Expected: {username}, Actual: {actual_email}"
    )
