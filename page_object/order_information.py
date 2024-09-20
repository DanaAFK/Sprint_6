import allure
from page_object.base_page import BasePage
from locators.locators_order_information import OrderInformationLocators


class OrderInformation(BasePage):

    @allure.title('Ожидание появления страницы с Информацией о заказе')
    def is_order_info_displayed(self):
        return self.is_element_displayed(OrderInformationLocators.ORDER_STATUS_INFO)
