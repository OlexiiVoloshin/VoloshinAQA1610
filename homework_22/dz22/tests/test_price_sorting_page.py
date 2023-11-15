import time
from homework_22.dz22.pages.price_sorting_page import PriceSortingPage


def test_price_filtering(driver, base_url, expected_filtered_url):
    price_from = 100
    price_to = 500

    driver.get(base_url)
    price_page = PriceSortingPage(driver)
    price_page.navigate_to_category_and_select()
    time.sleep(3)
    price_page.apply_price_filter(price_from, price_to)
    time.sleep(3)

    assert (
        driver.current_url == expected_filtered_url
    ), "URL-адреса не відповідає очікуваній після застосування фільтрів ціни"
