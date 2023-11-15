import time
from homework_22.dz22.pages.search_page import SearchPage


def test_search_functionality(driver, base_url, search_query):
    driver.get(base_url)
    search_page = SearchPage(driver)
    time.sleep(3)
    search_page.activate_search()
    time.sleep(3)
    search_page.search(search_query)

    assert search_query in driver.current_url, "URL-адреса не містить пошуковий запит"
