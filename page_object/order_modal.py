import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators_order_modal import OrderModalLocators
from selenium.webdriver.support import expected_conditions as EC


class OrderModal:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.title('Ожидание окна Хотите оформить заказ?')
    def confirm_order(self):
        self.wait.until(EC.visibility_of_element_located(OrderModalLocators.CONFIRM_MODAL))

        self.driver.find_element(*OrderModalLocators.CONFIRM_YES_BUTTON).click()

    @allure.title('Ожидание что окно Заказ оформлен появляется')
    def is_order_confirmed(self):
        self.wait.until(EC.visibility_of_element_located(OrderModalLocators.ORDER_MODAL))
        return self.driver.find_element(*OrderModalLocators.ORDER_MODAL).is_displayed()

    @allure.title('Нажатие на кнопку Посмотреть статус')
    def look_order_information(self):
        self.driver.find_element(*OrderModalLocators.LOOK_ORDER_INFO_BUTTON).click()