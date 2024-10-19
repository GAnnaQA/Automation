from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.epic('Форма Data types')
@allure.feature('Заполнение формы')
class form_filling:
    """
    Этот класс включает методы для заполнения интенет-формы Data types.
    """
    @allure.step('Открытие страницы с формой')
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу формы
        """
        self._driver = browser
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/data-types.html'
            )

    @allure.step('Ввод {name} в поле ввода First Name')
    def enter_the_first_name(self, name: str):
        """
        Находит поле ввода First Name и вводит в него Имя пользователя
        """
        first_name_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='first-name']"
            )
        first_name_input.send_keys(name)

    @allure.step('Ввод {lastname} в поле ввода Last Name')
    def enter_the_last_name(self, lastname: str):
        """
        Находит поле ввода Last Name и вводит в него Фамилию пользователя
        """
        last_name_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='last-name']"
            )
        last_name_input.send_keys(lastname)

    @allure.step('Ввод {address} в поле ввода Address')
    def enter_the_address(self, address: str):
        """
        Находит поле ввода Address и вводит в него адрес пользователя
        """
        address_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='address']"
            )
        address_input.send_keys(address)

    @allure.step('Ввод {city} в поле ввода City')
    def enter_the_city(self, city: str):
        """
        Находит поле ввода City и вводит в него город пользователя
        """
        city_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='city']"
            )
        city_input.send_keys(city)

    @allure.step('Ввод {country} в поле ввода Country')
    def enter_the_country(self, country: str):
        """
        Находит поле ввода Country и вводит в него страну пользователя
        """
        country_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='country']"
            )
        country_input.send_keys(country)

    @allure.step('Ввод {email} в поле ввода E-mail')
    def enter_the_email(self, email: str):
        """
        Находит поле ввода E-mail и вводит в него email пользователя
        """
        email_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='e-mail']"
            )
        email_input.send_keys(email)

    @allure.step('Ввод {phone} в поле ввода Phone number')
    def enter_the_phone(self, phone: str):
        """
        Находит поле ввода Phone number и вводит в него номер телефона пользователя
        """
        phone_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='phone']"
            )
        phone_input.send_keys(phone)

    @allure.step('Ввод {jobPosition} в поле ввода Job position')
    def enter_the_jobPos(self, jobPosition: str):
        """
        Находит поле ввода Job position и вводит в него должность пользователя
        """
        jobPos_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='job-position']"
            )
        jobPos_input.send_keys(jobPosition)

    @allure.step('Ввод {company} в поле ввода Сompany')
    def enter_the_company(self, company: str):
        """
        Находит поле ввода Сompany и вводит в него компанию пользователя
        """
        company_input = self._driver.find_element(
            By.CSS_SELECTOR, "input[name='company']"
            )
        company_input.send_keys(company)

    @allure.step('Нажатие кнопки Submit')
    def click_on_the_button(self):
        """
        Ждет, пока кнопка Submit будет доступна для клика и нажимает на нее
        """
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
