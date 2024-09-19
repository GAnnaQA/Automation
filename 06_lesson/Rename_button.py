from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/textinput")

input = driver.find_element(By.CSS_SELECTOR, "input#newButtonName")
input.send_keys("SkyPro")

button = driver.find_element(By.CSS_SELECTOR, "button#updatingButton")
button.click()
text = button.text
print(text)

driver.quit()
