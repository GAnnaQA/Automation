from selenium.webdriver.common.by import By
import allure


@allure.epic('Интернет-магазин')
@allure.feature('Оформление заказа')
class total:
    """
    Этот класс включает методы для взаимодействия со страницей подтверждения заказа в интернет-магазине.
    """
    def __init__(self, browser: str):
        """
        Открывает браузер и страницу с информацией о заказе.
        Данная страница для проверки заказа и его подтверждения
        Устанавливает полноэкранный режим
        """
        self._driver = browser
        self._driver.get('https://www.saucedemo.com/checkout-step-two.html')
        self._driver.maximize_window()
        self._driver.implicitly_wait(4)

    @allure.step('Получение финальной суммы заказа из поля Total')
    def get_total(self) -> str:
        """
        Находит и возвращает сумму заказа
        """
        total = self._driver.find_element(
            By.CSS_SELECTOR, 'div.summary_total_label'
            ).text
        return total
