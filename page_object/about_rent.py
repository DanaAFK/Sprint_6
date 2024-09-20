import allure
from page_object.base_page import BasePage
from locators.locators_about_rent import AboutRentLocators

class AboutRent(BasePage):

    @allure.title('Заполнение данных в форме Про Аренду')
    def fill_rent_details(self, rent_date):
        self.input_text(AboutRentLocators.RENT_DATE, rent_date)
        self.click_element(AboutRentLocators.RENT_PERIOD_FIELD)
        self.click_element(AboutRentLocators.RENT_PERIOD_TWO_DAYS)
        self.click_element(AboutRentLocators.COLOR_BLACK_CHECKBOX)

    @allure.title('Ожидание и клик по кнопке "Заказать"')
    def click_order(self):
        self.click_element(AboutRentLocators.ORDER_BUTTON)