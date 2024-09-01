from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


gdr_path = 'C:\\Users\\Anna\\Desktop\\обучение\\автоматизация\\geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.IeService(gdr_path))

driver.get('http://the-internet.herokuapp.com/login')

search_sel1 = "#username"
search_input1 = driver.find_element(By.CSS_SELECTOR, search_sel1)
search_input1.send_keys("tomsmith")

search_sel2 = "#password"
search_input2 = driver.find_element(By.CSS_SELECTOR, search_sel2)
search_input2.send_keys("SuperSecretPassword!")

search_sel3 = "button[type = 'submit']"
search_button = driver.find_element(By.CSS_SELECTOR, search_sel3)
search_button.click()

sleep(5)

driver.quit()
