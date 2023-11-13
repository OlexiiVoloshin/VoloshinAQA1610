import time
from homework_21.pages.price_sorting_page import PriceSortingPage


def test_price_sorting(driver):
    base_url = "https://makeup.com.ua/ua/"
    expected_url = (
        "https://makeup.com.ua/ua/categorys/255059/#price_from=100&price_to=500"
    )

    driver.get(base_url)
    sorting_page = PriceSortingPage(driver)

    sorting_page.navigate_to_category_and_select()
    time.sleep(3)
    sorting_page.apply_price_filter(100, 500)
    time.sleep(3)

    assert (
        driver.current_url == expected_url
    ), "URL-адреса не відповідає очікуваній URL-адресі з фільтрами цін"
