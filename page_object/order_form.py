import allure
from locators.locators_order_form import OrderFormLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderForm:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 30)

    @allure.title('Заполнение данных на странице Для кого Самокат')
    def fill_order_form(self, name, surname, address, phone):
        name_field = self.wait.until(EC.visibility_of_element_located(OrderFormLocators.NAME_FIELD))
        name_field.clear()
        name_field.send_keys(name)

        surname_field = self.wait.until(EC.visibility_of_element_located(OrderFormLocators.SURNAME_FIELD))
        surname_field.clear()
        surname_field.send_keys(surname)

        address_field = self.wait.until(EC.visibility_of_element_located(OrderFormLocators.ADDRESS_FIELD))
        address_field.clear()
        address_field.send_keys(address)

        metro_field = self.wait.until(EC.visibility_of_element_located(OrderFormLocators.METRO_FIELD))
        metro_field.click()

        metro_option = self.wait.until(EC.element_to_be_clickable(OrderFormLocators.METRO_ROKOSSOVSKOGO))
        metro_option.click()

        phone_field = self.wait.until(EC.visibility_of_element_located(OrderFormLocators.PHONE_FIELD))
        phone_field.clear()
        phone_field.send_keys(phone)

    @allure.title('Нажать на кнопку Далее')
    def click_further(self):
        further_button = self.wait.until(EC.visibility_of_element_located(OrderFormLocators.FURTHER_BUTTON))
        further_button.click()