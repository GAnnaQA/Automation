from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/classattr")

try:
    button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, '.btn.btn-primary.btn-test')
            )
    )
    # Если кнопка найдена, выполнить действие
    button.click()
    print("Кнопка найдена и нажата!")
except TimeoutError:
    # Если кнопка не найдена за отведенное время, вывести сообщение
    print("Кнопка не найдена за отведенное время")
