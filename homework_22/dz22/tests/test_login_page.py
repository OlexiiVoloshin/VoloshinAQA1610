import time
from homework_22.dz22.pages.login_page import LoginPage


def test_login_functionality(driver, base_url, login_credentials):
    driver.get(base_url)
    login_page = LoginPage(driver)

    login_page.login(login_credentials["username"], login_credentials["password"])
    time.sleep(3)

    login_page.navigate_to_account()
    actual_email = login_page.get_email_value()
    assert (
        actual_email == login_credentials["username"]
    ), "Електронна адреса на сторінці облікового запису не відповідає очікуваній"
