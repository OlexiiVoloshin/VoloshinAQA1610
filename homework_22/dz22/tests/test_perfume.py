import time
from homework_22.dz22.pages.perfume_page import PerfumePage


def test_perfume_page_navigation(driver):
    base_url = "https://makeup.com.ua/ua/"
    expected_url = "https://makeup.com.ua/ua/categorys/3/"

    driver.get(base_url)
    time.sleep(3)
    perfume_page = PerfumePage(driver)
    perfume_page.navigate_to_perfume_page()

    assert (
        driver.current_url == expected_url
    ), "URL-адреса не відповідає очікуваній URL-адресі сторінки парфумів"
