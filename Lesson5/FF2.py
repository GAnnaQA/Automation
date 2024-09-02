from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


gdr_path = 'C:\\Users\\Anna\\Desktop\\обучение\\автоматизация\\geckodriver.exe'
driver = webdriver.Firefox(service=webdriver.IeService(gdr_path))

driver.get('http://the-internet.herokuapp.com/inputs')

search_sel = "//input[@type='number']"
search_input = driver.find_element(By.XPATH, search_sel)
search_input.send_keys(1000)

search_input.clear()

search_input.send_keys(999)

sleep(5)

driver.quit()
