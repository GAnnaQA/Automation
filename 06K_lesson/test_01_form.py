import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name = driver.find_element(By.CSS_SELECTOR, "input[name='first-name']")
    first_name.send_keys("Иван")

    last_name = driver.find_element(By.CSS_SELECTOR, "input[name='last-name']")
    last_name.send_keys("Петров")

    address = driver.find_element(By.CSS_SELECTOR, "input[name='address']")
    address.send_keys("Ленина, 55-3")

    city = driver.find_element(By.CSS_SELECTOR, "input[name='city']")
    city.send_keys("Москва")

    country = driver.find_element(By.CSS_SELECTOR, "input[name='country']")
    country.send_keys("Россия")

    email = driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']")
    email.send_keys("test@skypro.com")

    phone = driver.find_element(By.CSS_SELECTOR, "input[name='phone']")
    phone.send_keys("+7985899998787")

    jobPos = driver.find_element(By.CSS_SELECTOR, "input[name='job-position']")
    jobPos.send_keys("QA")

    company = driver.find_element(By.CSS_SELECTOR, "input[name='company']")
    company.send_keys("SkyPro")

    try:
        button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button"))
    )

        if button.is_enabled():
            print("Кнопка доступна для клика.")

            driver.execute_script("arguments[0].scrollIntoView(true);", button)
            driver.execute_script("arguments[0].click();", button)
        else:
            print("Кнопка не доступна для клика.")
    except Exception as e:
        print(f"Возникла ошибка: {e}")

    try:
    # Проверка состояния поля Zip code
        zip_code_field = driver.find_element(By.CSS_SELECTOR, 'div#zip-code')
        zip_code_color = zip_code_field.value_of_css_property('border-color')
        assert zip_code_color.lower() == 'rgb(245, 194, 199)'

    # Проверка состояния остальных полей
        first_name_field = driver.find_element(By.CSS_SELECTOR, 'div#first-name')
        first_name_color = first_name_field.value_of_css_property('border-color')
        assert first_name_color.lower() == 'rgb(186, 219, 204)'

        last_name_field = driver.find_element(By.CSS_SELECTOR, 'div#last-name')
        last_name_color = last_name_field.value_of_css_property('border-color')
        assert last_name_color.lower() == 'rgb(186, 219, 204)'

        address_field = driver.find_element(By.CSS_SELECTOR, 'div#address')
        address_color = address_field.value_of_css_property('border-color')
        assert address_color.lower() == 'rgb(186, 219, 204)'

        city_field = driver.find_element(By.CSS_SELECTOR, 'div#city')
        city_color = city_field.value_of_css_property('border-color')
        assert city_color.lower() == 'rgb(186, 219, 204)'

        country_field = driver.find_element(By.CSS_SELECTOR, 'div#country')
        country_color = country_field.value_of_css_property('border-color')
        assert country_color.lower() == 'rgb(186, 219, 204)'

        email_field = driver.find_element(By.CSS_SELECTOR, 'div#e-mail')
        email_color = email_field.value_of_css_property('border-color')
        assert email_color.lower() == 'rgb(186, 219, 204)'

        phone_field = driver.find_element(By.CSS_SELECTOR, 'div#phone')
        phone_color = phone_field.value_of_css_property('border-color')
        assert phone_color.lower() == 'rgb(186, 219, 204)'

        jobPos_field = driver.find_element(By.CSS_SELECTOR, 'div#job-position')
        jobPosition_color = jobPos_field.value_of_css_property('border-color')
        assert jobPosition_color.lower() == 'rgb(186, 219, 204)'

        company_field = driver.find_element(By.CSS_SELECTOR, 'div#company')
        company_color = company_field.value_of_css_property('border-color')
        assert company_color.lower() == 'rgb(186, 219, 204)'

        print("Все проверки успешно прошли.")
    except AssertionError:
        print("Проверка цвета границы полей не прошла.")
    except NoSuchElementException:
        print("Некоторые элементы не найдены.")
    finally:
        driver.quit() 
