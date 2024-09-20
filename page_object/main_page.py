import allure
from page_object.base_page import BasePage
from locators.locators_main_page import MainPageLocators


class MainPage(BasePage):

    @allure.title('Клик по кнопкам Заказать в шапке страницы и снизу формы')
    def click_order_button(self, button_number):
        if button_number == 1:
            self.click_element(MainPageLocators.ORDER_BUTTON_1)
        elif button_number == 2:
            self.click_element(MainPageLocators.ORDER_BUTTON_2)

    @allure.title('Клик по лого Самокат')
    def click_samokat_logo(self):
        self.click_element(MainPageLocators.SAMOKAT_LOGO)

    @allure.title('Ожидание появления Главной страницы')
    def is_home_page_open(self):
        return self.is_element_displayed(MainPageLocators.HOME_PAGE)

    @allure.title('Клик по лого Яндекс')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.title('Ожидание появления страницы Дзен')
    def is_dzen_page_open(self):
        return self.is_element_displayed(MainPageLocators.HOME_PAGE)

