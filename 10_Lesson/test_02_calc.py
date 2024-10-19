from selenium import webdriver
from pages.main_calc_page import calc
import allure


time = '45'


@allure.id('Calc_1')
@allure.feature('Plus')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка получения результата через установленное время')
@allure.description(
    'В строке "This calculator waits _ ..." устанавливается время в секундах. На калькуляторе производится сложение 2х чисел. После нажатия кнопки "=" начинается отсчет установленного времени. Спустя это время проверяется вывод результата сложения.')
def test_calc():
    driver = webdriver.Chrome()
    calculator = calc(driver)
    calculator.input_delay(time)
    calculator.click_seven()
    calculator.click_plus()
    calculator.click_eight()
    calculator.click_equal()
    result = calculator.get_result(time)
    driver.quit()
    with allure.step('Проверка полученного результата'):
        assert result == 15
