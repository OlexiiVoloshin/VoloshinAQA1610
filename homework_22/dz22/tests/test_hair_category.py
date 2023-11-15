import time
from homework_22.dz22.pages.hair_category_page import HairCategoryPage


def test_hair_category_filtering(driver, base_url, expected_url):
    driver.get(base_url)
    hair_page = HairCategoryPage(driver)

    hair_page.navigate_to_hair_category()
    hair_page.apply_filters()
    time.sleep(3)

    assert (
        driver.current_url == expected_url
    ), "URL-адреса не відповідає очікуваній URL-адресі з застосованими фільтрами"
