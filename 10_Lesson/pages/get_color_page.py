from selenium.webdriver.common.by import By
import allure


@allure.epic('Форма Data types')
@allure.feature('Проверка результата заполнения')
class get_color:
    """
    Этот класс включает методы для получения цвета полей интенет-формы Data types после заполнения.
    """

    def __init__(self, browser: str):
        self._driver = browser

    @allure.step('Получение цвета поля Zip code из CSS')
    def get_color_zip_code(self) -> str:
        """
        Возвращает цвет поля Zip code в формате RGB
        """
        zip_code_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#zip-code'
            )
        zip_code_color = zip_code_field.value_of_css_property(
            'border-color')
        return zip_code_color

    @allure.step('Получение цвета поля First name из CSS')
    def get_color_first_name(self) -> str:
        """
        Возвращает цвет поля First name в формате RGB
        """
        first_name_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#first-name')
        first_name_color = first_name_field.value_of_css_property(
            'border-color')
        return first_name_color

    @allure.step('Получение цвета поля Last name из CSS')
    def get_color_last_name(self) -> str:
        """
        Возвращает цвет поля Last name в формате RGB
        """
        last_name_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#last-name')
        last_name_color = last_name_field.value_of_css_property(
            'border-color')
        return last_name_color

    @allure.step('Получение цвета поля Address из CSS')
    def get_color_address(self) -> str:
        """
        Возвращает цвет поля Address в формате RGB
        """
        address_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#address')
        address_color = address_field.value_of_css_property(
            'border-color')
        return address_color

    @allure.step('Получение цвета поля City из CSS')
    def get_color_city(self) -> str:
        """
        Возвращает цвет поля City в формате RGB
        """
        city_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#city')
        city_color = city_field.value_of_css_property(
            'border-color')
        return city_color

    @allure.step('Получение цвета поля Country из CSS')
    def get_color_country(self) -> str:
        """
        Возвращает цвет поля Country в формате RGB
        """
        country_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#country')
        country_color = country_field.value_of_css_property(
            'border-color')
        return country_color

    @allure.step('Получение цвета поля E-mail из CSS')
    def get_color_email(self) -> str:
        """
        Возвращает цвет поля E-mail в формате RGB
        """
        email_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#e-mail')
        email_color = email_field.value_of_css_property(
            'border-color')
        return email_color

    @allure.step('Получение цвета поля Phone number из CSS')
    def get_color_phone(self) -> str:
        """
        Возвращает цвет поля Phone number в формате RGB
        """
        phone_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#phone')
        phone_color = phone_field.value_of_css_property(
            'border-color')
        return phone_color

    @allure.step('Получение цвета поля Job position из CSS')
    def get_color_jobPos(self) -> str:
        """
        Возвращает цвет поля Job position в формате RGB
        """
        jobPos_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#job-position')
        jobPosition_color = jobPos_field.value_of_css_property(
            'border-color')
        return jobPosition_color

    @allure.step('Получение цвета поля Company из CSS')
    def get_color_company(self) -> str:
        """
        Возвращает цвет поля Company в формате RGB
        """
        company_field = self._driver.find_element(
            By.CSS_SELECTOR, 'div#company')
        company_color = company_field.value_of_css_property(
            'border-color')
        return company_color
