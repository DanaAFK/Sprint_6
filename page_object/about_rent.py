import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators_about_rent import AboutRentLocators
from selenium.webdriver.support import expected_conditions as EC


class AboutRent:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.title('Заполнение данных в форме Про Френду')
    def fill_rent_details(self, rent_date):
        rent_date_field = self.wait.until(EC.visibility_of_element_located(AboutRentLocators.RENT_DATE))
        rent_date_field.click()
        rent_date_field.send_keys(rent_date)

        rent_period_field = self.wait.until(EC.visibility_of_element_located(AboutRentLocators.RENT_PERIOD_FIELD))
        rent_period_field.click()

        rent_period_two_days = self.wait.until(EC.visibility_of_element_located(AboutRentLocators.RENT_PERIOD_TWO_DAYS))
        rent_period_two_days.click()

        color_black_checkbox = self.wait.until(EC.visibility_of_element_located(AboutRentLocators.COLOR_BLACK_CHECKBOX))
        color_black_checkbox.click()

    @allure.title('Ожидание и клик по кнопке "Заказать')
    def click_order(self):
        order_button = self.wait.until(EC.visibility_of_element_located(AboutRentLocators.ORDER_BUTTON))
        order_button.click()