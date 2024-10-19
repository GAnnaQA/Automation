from selenium.webdriver.common.by import By
import allure


@allure.epic('Интернет-магазин')
@allure.feature('Корзина')
class shopping_cart:
    """
    Этот класс включает методы для взаимодействия с корзиной пользователя в интернет-магазине.
    """
    @allure.step('Открытиз страницы корзины')
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу корзины пользователя
        Устанавливает полноэкранный режим
        """
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/cart.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    @allure.step('Нажатие кнопки Checkout')
    def click_checkout(self):
        """
        Находит кнопку Checkout и нажимает на нее
        Происходит переход на страницу ввода данных для оформления заказа
        """
        checkout = self._driver.find_element(
            By.CSS_SELECTOR, 'button#checkout'
            )
        checkout.click()
