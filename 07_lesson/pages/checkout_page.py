from selenium.webdriver.common.by import By


class checkout_step_one:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def enter_the_firstName(self, firstName):
        first_Name = self._driver.find_element(
            By.CSS_SELECTOR, 'input#first-name'
            )
        first_Name.send_keys(firstName)

    def enter_the_lastName(self, lastName):
        last_Name = self._driver.find_element(
            By.CSS_SELECTOR, 'input#last-name'
            )
        last_Name.send_keys(lastName)

    def enter_the_postalCode(self, postalCode):
        postal_Code = self._driver.find_element(
            By.CSS_SELECTOR, 'input#postal-code'
            )
        postal_Code.send_keys(postalCode)

    def click_continueButton(self):
        continueButton = self._driver.find_element(
            By.CSS_SELECTOR, 'input#continue'
            )
        continueButton.click()
