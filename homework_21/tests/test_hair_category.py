import time
from homework_21.pages.hair_category_page import HairCategoryPage


def test_hair_category_filtering(driver):
    base_url = "https://makeup.com.ua/ua/"
    expected_url = "https://makeup.com.ua/ua/categorys/20272/#o[2243][]=40165&o[2245][]=45031&o[2257][]=24219"

    driver.get(base_url)
    hair_page = HairCategoryPage(driver)

    hair_page.navigate_to_hair_category()
    hair_page.apply_filters()
    time.sleep(3)  # Allow time for filters to apply and URL to update

    assert driver.current_url == expected_url, (
        "URL-адреса не відповідає очікуваній URL-адресі з застосованими " "фільтрами"
    )
