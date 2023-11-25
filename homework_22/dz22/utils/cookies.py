class Cookies:
    def __init__(self, driver):
        self.driver = driver

    def get_cookie(self, name):
        return self.driver.get_cookie(name)

    def set_cookie(self, cookie_dict):
        self.driver.add_cookie(cookie_dict)

    def delete_cookie(self, name):
        self.driver.delete_cookie(name)

    def get_all_cookies(self):
        return self.driver.get_cookies()
