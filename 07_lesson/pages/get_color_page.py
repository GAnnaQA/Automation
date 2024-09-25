from selenium.webdriver.common.by import By


class get_color:

    def __init__(self, browser):
        self._driver = browser

    def get_color_zip_code(self):
        zip_code_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#zip-code'
            )
        zip_code_color = zip_code_field.value_of_css_property(
            'border-color')
        return zip_code_color

    def get_color_first_name(self):
        first_name_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#first-name')
        first_name_color = first_name_field.value_of_css_property(
            'border-color')
        return first_name_color

    def get_color_last_name(self):
        last_name_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#last-name')
        last_name_color = last_name_field.value_of_css_property(
            'border-color')
        return last_name_color

    def get_color_address(self):
        address_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#address')
        address_color = address_field.value_of_css_property(
            'border-color')
        return address_color

    def get_color_city(self):
        city_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#city')
        city_color = city_field.value_of_css_property(
            'border-color')
        return city_color

    def get_color_country(self):
        country_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#country')
        country_color = country_field.value_of_css_property(
            'border-color')
        return country_color

    def get_color_email(self):
        email_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#e-mail')
        email_color = email_field.value_of_css_property(
            'border-color')
        return email_color

    def get_color_phone(self):
        phone_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#phone')
        phone_color = phone_field.value_of_css_property(
            'border-color')
        return phone_color

    def get_color_jobPos(self):
        jobPos_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#job-position')
        jobPosition_color = jobPos_field.value_of_css_property(
            'border-color')
        return jobPosition_color

    def get_color_company(self):
        company_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#company')
        company_color = company_field.value_of_css_property(
            'border-color')
        return company_color
