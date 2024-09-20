import allure
from page_object.base_page import BasePage
from locators.locators_order_modal import OrderModalLocators


class OrderModal(BasePage):

    @allure.title('Ожидание окна Хотите оформить заказ?')
    def confirm_order(self):
        self.find_element(OrderModalLocators.CONFIRM_MODAL)
        self.click_element(OrderModalLocators.CONFIRM_YES_BUTTON)

    @allure.title('Ожидание что окно Заказ оформлен появляется')
    def is_order_confirmed(self):
        return self.is_element_displayed(OrderModalLocators.ORDER_MODAL)

    @allure.title('Нажатие на кнопку Посмотреть статус')
    def look_order_information(self):
        self.click_element(OrderModalLocators.LOOK_ORDER_INFO_BUTTON)
