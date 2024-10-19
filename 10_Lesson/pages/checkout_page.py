from selenium.webdriver.common.by import By
import allure


@allure.epic('Интернет-магазин')
@allure.feature('Оформление заказа')
class checkout_step_one:
    """
    Этот класс включает методы для заполнения данных для заказа в интернет магазине.
    Для оформления заказа необходимо ввести Имя и Фамилию пользователя и Индекс.
    После нажать кнопку Continue.
    """
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу ввода данных для оформления заказа
        Устанавливает полноэкранный режим
        """
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/checkout-step-one.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    @allure.step('Ввод {firstName} в поле ввода First Name')
    def enter_the_firstName(self, firstName: str):
        """
        Находит поле ввода First Name и вводит в него Имя пользователя
        """
        first_Name = self._driver.find_element(
            By.CSS_SELECTOR, 'input#first-name'
            )
        first_Name.send_keys(firstName)

    @allure.step('Ввод {lastName} в поле ввода Last Name')
    def enter_the_lastName(self, lastName: str):
        """
        Находит поле ввода Last Name и вводит в него Фамилию пользователя
        """
        last_Name = self._driver.find_element(
            By.CSS_SELECTOR, 'input#last-name'
            )
        last_Name.send_keys(lastName)

    @allure.step('Ввод {postalCode} в поле ввода ZIP_Postal code')
    def enter_the_postalCode(self, postalCode: int):
        """
        Находит поле ввода ZIP_Postal code и вводит в него Индекс пользователя
        """
        postal_Code = self._driver.find_element(
            By.CSS_SELECTOR, 'input#postal-code'
            )
        postal_Code.send_keys(postalCode)

    @allure.step('Нажатие кнопки Continue')
    def click_continueButton(self):
        """
        Находит элемент кнопки Continue и нажимает на нее
        """
        continueButton = self._driver.find_element(
            By.CSS_SELECTOR, 'input#continue'
            )
        continueButton.click()
