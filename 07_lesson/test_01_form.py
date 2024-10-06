from selenium import webdriver
from pages.form_filling_page import form_filling
from pages.get_color_page import get_color


def test_form():
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
    assert zip_code_color == 'rgb(245, 194, 199)'
    assert first_name_color == 'rgb(186, 219, 204)'
    assert last_name_color == 'rgb(186, 219, 204)'
    assert address_color == 'rgb(186, 219, 204)'
    assert city_color == 'rgb(186, 219, 204)'
    assert country_color == 'rgb(186, 219, 204)'
    assert phone_color == 'rgb(186, 219, 204)'
    assert email_color == 'rgb(186, 219, 204)'
    assert jobPos_color == 'rgb(186, 219, 204)'
    assert company_color == 'rgb(186, 219, 204)'
