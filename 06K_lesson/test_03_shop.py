from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)


driver.get('https://www.saucedemo.com/')

user_name = driver.find_element(By.CSS_SELECTOR, 'input#user-name')
user_name.send_keys('standard_user')

password = driver.find_element(By.CSS_SELECTOR, 'input#password')
password.send_keys('secret_sauce')

login_button = driver.find_element(By.CSS_SELECTOR, 'input#login-button')
login_button.click()

backpack = driver.find_element(
    By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-backpack'
    )
backpack.click()

T_Shirt = driver.find_element(
    By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-bolt-t-shirt'
    )
T_Shirt.click()

Onesie = driver.find_element(
    By.CSS_SELECTOR, 'button#add-to-cart-sauce-labs-onesie'
    )
Onesie.click()

shopping_cart = driver.find_element(By.CSS_SELECTOR, 'a.shopping_cart_link')
shopping_cart.click()

checkout = driver.find_element(By.CSS_SELECTOR, 'button#checkout')
checkout.click()

firstName = driver.find_element(By.CSS_SELECTOR, 'input#first-name')
firstName.send_keys('Anna')

lastName = driver.find_element(By.CSS_SELECTOR, 'input#last-name')
lastName.send_keys('Gruzdeva')

postalCode = driver.find_element(By.CSS_SELECTOR, 'input#postal-code')
postalCode.send_keys('601012')

continueButton = driver.find_element(By.CSS_SELECTOR, 'input#continue')
continueButton.click()

total = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text

assert total == 'Total: $58.29'

driver.quit()
