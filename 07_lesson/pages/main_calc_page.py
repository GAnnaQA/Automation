from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class calc:
    def __init__(self, browser):
        self._driver = browser
        self._driver.implicitly_wait(4)
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
            )

    def input_delay(self, time):
        input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input#delay')
        input_delay.clear()
        input_delay.send_keys(time)

    def click_seven(self):
        seven = self._driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-primary" and text()="7"]'
            )
        seven.click()

    def click_plus(self):
        plus = self._driver.find_element(
            By.XPATH,
            '//span[@class="operator btn btn-outline-success" and text()="+"]'
            )
        plus.click()

    def click_eight(self):
        eight = self._driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-primary" and text()="8"]'
            )
        eight.click()

    def click_equal(self):
        equal = self._driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-warning" and text()="="]'
            )
        equal.click()

    def get_result(self, time):
        try:
            wait = WebDriverWait(self._driver, time)
            wait.until(EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, 'div.screen'), '15'
                ))
        except TimeoutException:
            result = False
        else:
            result = self._driver.find_element(
                By.CSS_SELECTOR, 'div.screen'
                ).text
        return result
