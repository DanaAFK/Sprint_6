import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators_order_information import OrderInformationLocators


class OrderInformation:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.title('Ожидание появления страницы с Информацией о заказе')
    def is_order_info_displayed(self):
        return self.driver.find_element(*OrderInformationLocators.ORDER_STATUS_INFO).is_displayed()