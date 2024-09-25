from selenium.webdriver.common.by import By


class shopping_cart:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def click_checkout(self):
        checkout = self._driver.find_element(
            By.CSS_SELECTOR, 'button#checkout'
            )
        checkout.click()
