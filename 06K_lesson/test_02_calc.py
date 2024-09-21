from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException


driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)


driver.get(
    'https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html'
    )

input_delay = driver.find_element(By.CSS_SELECTOR, '#delay')
input_delay.clear()
input_delay.send_keys('45')

seven = driver.find_element(
    By.XPATH, '//span[@class="btn btn-outline-primary" and text()="7"]'
    )
seven.click()

plus = driver.find_element(
    By.XPATH,
    '//span[@class="operator btn btn-outline-success" and text()="+"]'
    )
plus.click()

eight = driver.find_element(
    By.XPATH, '//span[@class="btn btn-outline-primary" and text()="8"]'
    )
eight.click()

equal = driver.find_element(
    By.XPATH, '//span[@class="btn btn-outline-warning" and text()="="]'
    )
equal.click()

try:
    wait = WebDriverWait(driver, 45)
    wait.until(
        lambda x: x.find_element(
            By.XPATH, "//div[@class='screen' and text()='15']"
            )
            )
except TimeoutException:
    result = False
    print('Отвал по таймауту')
else:
    result = driver.find_element(By.CSS_SELECTOR, 'div.screen').text
    print('Дождались')

assert result == "15"

driver.quit()
