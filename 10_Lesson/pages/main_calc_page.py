from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import allure


@allure.epic('Калькулятор')
@allure.feature('Проверка результата вычисления')
class calc:
    """
    Этот класс включает методы для работы с калькулятором.
    """
    @allure.step('Открытие страница калькулятора')
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу калькулятора
        """
        self._driver = browser
        self._driver.implicitly_wait(4)
        self._driver.get(
            'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
            )

    @allure.step('Ввод времени ожидания')
    def input_delay(self, time: str):
        """
        Находит поле ввода в строке This calculator waits _ ...
        Очищает поле ввода.
        Вводит в поле ввода заданное время в секундах.
        """
        with allure.step('Поиск поля ввода #delay'):
            input_delay = self._driver.find_element(By.CSS_SELECTOR, 'input#delay')
        with allure.step('Очищение поля ввода #delay'):
            input_delay.clear()
        with allure.step('Ввод значения в секундах в поле ввода #delay'):
            input_delay.send_keys(time)

    @allure.step('Нажатие кнопки калькулятора 7')
    def click_seven(self):
        """
        Нажимает на кнопку калькулятора 7
        """
        seven = self._driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-primary" and text()="7"]'
            )
        seven.click()

    @allure.step('Нажатие кнопки калькулятора +')
    def click_plus(self):
        """
        Нажимает на кнопку калькулятора +
        """
        plus = self._driver.find_element(
            By.XPATH,
            '//span[@class="operator btn btn-outline-success" and text()="+"]'
            )
        plus.click()

    @allure.step('Нажатие кнопки калькулятора 8')
    def click_eight(self):
        """
        Нажимает на кнопку калькулятора 8
        """
        eight = self._driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-primary" and text()="8"]'
            )
        eight.click()

    @allure.step('Нажатие кнопки калькулятора =')
    def click_equal(self):
        """
        Нажимает на кнопку калькулятора =
        """
        equal = self._driver.find_element(
            By.XPATH, '//span[@class="btn btn-outline-warning" and text()="="]'
            )
        equal.click()

    @allure.step('Получение результата вычислений через установленное время')
    def get_result(self, time: str) -> str:
        """
        Ждет заданное время в секундах.
        После получает результат вычисления калькулятора
        """
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
