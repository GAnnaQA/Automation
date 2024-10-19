from selenium import webdriver
from pages.form_filling_page import form_filling
from pages.get_color_page import get_color
import allure


@allure.id('Form_1')
@allure.feature('Error')
@allure.severity(allure.severity_level.CRITICAL)
@allure.title('Негативный тест на проверку обязательности поля Zip code')
@allure.description('Заполняются все поля формы, кроме поля Zip code. После нажатия на кнопку Submit проверяется, что поле Zip code окрашено в красный цвет')
def test_form():
    red = 'rgb(245, 194, 199)'
    gren = 'rgb(186, 219, 204)'
    browser = webdriver.Chrome()
    form_page = form_filling(browser)
    form_page.enter_the_first_name('Anna')
    form_page.enter_the_last_name('Gruzdeva')
    form_page.enter_the_address('Химшиашвили, 26')
    form_page.enter_the_city('Batumi')
    form_page.enter_the_country('Georgia')
    form_page.enter_the_phone('89999999999')
    form_page.enter_the_email('test@te.st')
    form_page.enter_the_jobPos('QA')
    form_page.enter_the_company('SkyPro')
    form_page.click_on_the_button()
    get_color_page = get_color(browser)
    zip_code_color = get_color_page.get_color_zip_code()
    first_name_color = get_color_page.get_color_first_name()
    last_name_color = get_color_page.get_color_last_name()
    address_color = get_color_page.get_color_address()
    city_color = get_color_page.get_color_city()
    country_color = get_color_page.get_color_country()
    phone_color = get_color_page.get_color_phone()
    email_color = get_color_page.get_color_email()
    jobPos_color = get_color_page.get_color_jobPos()
    company_color = get_color_page.get_color_company()
    browser.quit()
    with allure.step('Проверить, что цвет поля Zip code - {red}'):
        assert zip_code_color == red
    with allure.step('Проверить, что цвет поля First name - {gren}'):
        assert first_name_color == gren
    with allure.step('Проверить, что цвет поля Last name - {gren}'):
        assert last_name_color == gren
    with allure.step('Проверить, что цвет поля Address - {gren}'):
        assert address_color == gren
    with allure.step('Проверить, что цвет поля City - {gren}'):
        assert city_color == gren
    with allure.step('Проверить, что цвет поля Country - {gren}'):
        assert country_color == gren
    with allure.step('Проверить, что цвет поля Phone number - {gren}'):
        assert phone_color == gren
    with allure.step('Проверить, что цвет поля E-mail - {gren}'):
        assert email_color == gren
    with allure.step('Проверить, что цвет поля Job position - {gren}'):
        assert jobPos_color == gren
    with allure.step('Проверить, что цвет поля Company - {gren}'):
        assert company_color == gren
