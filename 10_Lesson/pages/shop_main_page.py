from selenium.webdriver.common.by import By
import allure


@allure.epic('Интернет-магазин')
@allure.feature('Каталог')
class shopping:
    """
    Этот класс включает методы для взаимодействия с каталогом товаров интернет-магазина.
    """
    @allure.step('Открытие страницы с каталогом товаров')
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу каталога товаров
        Устанавливает полноэкранный режим
        """
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/inventory.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    @allure.step('Добавление в корзину товара Backpack')
    def Buy_backpack(self):
        """
        Добавляет Backpack в корзину
        """
        backpack = self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack'
            )
        backpack.click()

    @allure.step('Добавление в корзину товара T-Shirt')
    def Buy_T_Shirt(self):
        """
        Добавляет T-Shirt в корзину
        """
        T_Shirt = self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt'
            )
        T_Shirt.click()

    @allure.step('Добавление в корзину товара Onesie')
    def Buy_Onesie(self):
        """
        Добавляет Onesie в корзину
        """
        Onesie = self._driver.find_element(
            By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie'
            )
        Onesie.click()

    @allure.step('Нажатие на иконку корзины')
    def click_shopping_cart_button(self):
        """
        Находит иконку корзины и нажимает на нее
        Происходит переход в корзину пользователя
        """
        shopping_cart_button = self._driver.find_element(
            By.CSS_SELECTOR, 'a.shopping_cart_link'
            )
        shopping_cart_button.click()
