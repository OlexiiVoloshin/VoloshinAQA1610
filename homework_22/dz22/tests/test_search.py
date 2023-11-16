from homework_22.dz22.pages.search_page import SearchPage


def test_search_functionality(driver, base_url, search_query):
    # Тестування функціональності пошуку
    driver.get(base_url)
    search_page = SearchPage(driver)
    search_page.activate_search()
    search_page.search(search_query)

    # Перевірка, чи URL містить пошуковий запит
    assert search_query in driver.current_url, "URL-адреса не містить пошуковий запит"
