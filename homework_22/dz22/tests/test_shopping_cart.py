from homework_22.dz22.pages.cart_page import CartPage


def test_add_to_cart(driver, base_url):
    # Тестування процесу додавання товару до кошика
    driver.get(base_url)
    cart_page = CartPage(driver)
    cart_page.navigate_to_clothing_category()
    cart_page.apply_men_filter()
    cart_page.select_product_and_buy()
    cart_page.close_popup_and_check_cart()

    # Перевірка, чи товар доданий до кошика
    assert cart_page.is_cart_popup_visible(), "Спливаюче вікно кошика не з’явилося"
