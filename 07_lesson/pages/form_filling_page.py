from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class form_filling:

    def __init__(self, browser):
        self._driver = browser
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
            )

    def enter_the_first_name(self, name):
        first_name_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='first-name']"
            )
        first_name_input.send_keys(name)

    def enter_the_last_name(self, lastname):
        last_name_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='last-name']"
            )
        last_name_input.send_keys(lastname)

    def enter_the_address(self, address):
        address_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='address']"
            )
        address_input.send_keys(address)

    def enter_the_city(self, city):
        city_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='city']"
            )
        city_input.send_keys(city)

    def enter_the_country(self, country):
        country_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='country']"
            )
        country_input.send_keys(country)

    def enter_the_email(self, email):
        email_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']"
            )
        email_input.send_keys(email)

    def enter_the_phone(self, phone):
        phone_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='phone']"
            )
        phone_input.send_keys(phone)

    def enter_the_jobPos(self, jobPosition):
        jobPos_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='job-position']"
            )
        jobPos_input.send_keys(jobPosition)

    def enter_the_company(self, company):
        company_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='company']"
            )
        company_input.send_keys(company)

    def click_on_the_button(self):
        button = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button")))
        if button.is_enabled():
            print("Кнопка доступна для клика.")

            self._driver.execute_script(
                "arguments[0].scrollIntoView(true);", button
                )
            self._driver.execute_script(
                "arguments[0].click();", button
                )
        else:
            print("Кнопка не доступна для клика.")
