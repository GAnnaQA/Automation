from selenium import webdriver
from pages.main_calc_page import calc


time = '45'


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
    assert result == time
