from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


gdr_path = 'C:\\Users\\Anna\\Desktop\\обучение\\автоматизация\\geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.IeService(gdr_path))

driver.get('http://the-internet.herokuapp.com/entry_ad')

sleep(2)

try:
    button = WebDriverWait(driver, 60).until(
        EC.presence_of_element_located(
            (By.XPATH, "//p[normalize-space(.)='Close']")
            )
    )
    # Если кнопка найдена, выполнить действие
    button.click()
    print("Кнопка найдена и нажата!")
except TimeoutError:
    # Если кнопка не найдена за отведенное время, вывести сообщение
    print("Кнопка не найдена за отведенное время")
driver.quit()
