from selenium.webdriver.common.by import By


class shopping:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def Buy_backpack(self):
        backpack = self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack'
            )
        backpack.click()

    def Buy_T_Shirt(self):
        T_Shirt = self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt'
            )
        T_Shirt.click()

    def Buy_Onesie(self):
        Onesie = self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie'
            )
        Onesie.click()

    def click_shopping_cart_button(self):
        shopping_cart_button = self._driver.find_element(
            By.CSS_SELECTOR, 'a.shopping_cart_link'
            )
        shopping_cart_button.click()
