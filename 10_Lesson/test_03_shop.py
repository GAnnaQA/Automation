from selenium import webdriver
from pages.auto_page import authorization
from pages.shop_main_page import shopping
from pages.shopping_cart_page import shopping_cart
from pages.checkout_page import checkout_step_one
from pages.total_page import total
import allure


@allure.id('Shop_1')
@allure.feature('Total_amount')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Проверка финальной суммы заказа')
@allure.description(
    'Проверяется финальная сумма заказа в интернет-магазине в поле Total'
    )
def test_shop():
    driver = webdriver.Chrome()
    auto = authorization(driver)
    auto.enter_the_user_name('standard_user')
    auto.enter_the_password('secret_sauce')
    auto.click_login_button()
    shop = shopping(driver)
    shop.Buy_backpack()
    shop.Buy_T_Shirt()
    shop.Buy_Onesie()
    cart = shopping_cart(driver)
    cart.click_checkout()
    checkout = checkout_step_one(driver)
    checkout.enter_the_firstName('Anna')
    checkout.enter_the_lastName('Gruzdeva')
    checkout.enter_the_postalCode('601000')
    checkout.click_continueButton()
    total_cost = total(driver)
    total_text = total_cost.get_total()
    with allure.step('Проверка финальной суммы заказа'):
        assert total_text == 'Total: $58.29'
    driver.quit()
