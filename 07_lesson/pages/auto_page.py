from selenium.webdriver.common.by import By


class authorization:
    def __init__(self, browser):
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    def enter_the_user_name(self, userName):
        user_name = self._driver.find_element(
            By.CSS_SELECTOR, 'input#user-name'
            )
        user_name.send_keys(userName)

    def enter_the_password(self, password):
        password_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input#password'
            )
        password_input.send_keys(password)

    def click_login_button(self):
        login_button = self._driver.find_element(
            By.CSS_SELECTOR, 'input#login-button'
            )
        login_button.click()
