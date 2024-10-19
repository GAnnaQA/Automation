from selenium.webdriver.common.by import By
import allure


@allure.epic('Интернет-магазин')
@allure.feature('Авторизация')
class authorization:
    """
    Этот класс включает методы для авторизации в интернет магазине.
    Для авторизации необходимы Имя пользователя и Пароль.
    После нажать кнопку Login.
    """
    @allure.step('Открытие страницы авторизации')
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу авторизации в магазине
        Устанавливает полноэкранный режим
        """
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    @allure.step('Ввод {userName} в поле ввода Username')
    def enter_the_user_name(self, userName: str):
        """
        Находит поле ввода Username и вводит в него Имя пользователя
        """
        user_name = self._driver.find_element(
            By.CSS_SELECTOR, 'input#user-name'
            )
        user_name.send_keys(userName)

    @allure.step('Ввод {password} в поле ввода Password')
    def enter_the_password(self, password: str):
        """
        Находит поле ввода Password и вводит в него пароль
        """
        password_input = self._driver.find_element(
            By.CSS_SELECTOR, 'input#password'
            )
        password_input.send_keys(password)

    @allure.step('Нажатие кнопки Login')
    def click_login_button(self):
        """
        Находит элемент кнопки Login и нажимает на нее
        """
        login_button = self._driver.find_element(
            By.CSS_SELECTOR, 'input#login-button'
            )
        login_button.click()
