from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException

driver = webdriver.Chrome()

try:
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
        )

    waiting = WebDriverWait(driver, 40)
    waiting.until(
        lambda d: len(d.find_elements(By.TAG_NAME, 'img')) == 5
        )

    third_image = driver.find_element(By.CSS_SELECTOR, 'img[alt="award"]')

    src = third_image.get_attribute('src')
    print(src)

except TimeoutException:
    print("Элемент не доступен в течение ожидания.")
except NoSuchElementException:
    print("Элемент с атрибутом 'alt=\"award\"' не найден.")
finally:
    driver.quit()
