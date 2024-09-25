from selenium.webdriver.common.by import By


class total:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def get_total(self):
        total = self._driver.find_element(
            By.CSS_SELECTOR, 'div.summary_total_label'
            ).text
        return total
