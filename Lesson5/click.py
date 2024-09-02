from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

for _ in range(5):
    button_sel = "button[onclick='addElement()']"
    button_add = driver.find_element(By.CSS_SELECTOR, button_sel)
    button_add.click()

button_del_sel = "button[onclick='deleteElement()']"
butten_delet = driver.find_elements(By.CSS_SELECTOR, button_del_sel)
print(len(butten_delet))
