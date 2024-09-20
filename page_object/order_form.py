import allure
from locators.locators_order_form import OrderFormLocators
from selenium.webdriver.support.ui import WebDriverWait
import allure
from page_object.base_page import BasePage


class OrderForm(BasePage):

    @allure.title('Заполнение данных на странице Для кого Самокат')
    def fill_order_form(self, name, surname, address, phone):
        self.input_text(OrderFormLocators.NAME_FIELD, name)
        self.input_text(OrderFormLocators.SURNAME_FIELD, surname)
        self.input_text(OrderFormLocators.ADDRESS_FIELD, address)

        self.click_element(OrderFormLocators.METRO_FIELD)
        self.click_element(OrderFormLocators.METRO_ROKOSSOVSKOGO)
        self.input_text(OrderFormLocators.PHONE_FIELD, phone)

    @allure.title('Нажать на кнопку Далее')
    def click_further(self):
        self.click_element(OrderFormLocators.FURTHER_BUTTON)
