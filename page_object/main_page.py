import allure
from selenium.webdriver.support.ui import WebDriverWait
from locators.locators_main_page import MainPageLocators
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.title('Клик по кнопкам Заказать в шапке страницы и снизу формы')
    def click_order_button(self, button_number):
        if button_number == 1:
            self.driver.find_element(*MainPageLocators.ORDER_BUTTON_1).click()
        elif button_number == 2:
            self.driver.find_element(*MainPageLocators.ORDER_BUTTON_2).click()

    @allure.title('Клик по лого Самокат')
    def click_samokat_logo(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.SAMOKAT_LOGO)).click()

    @allure.title('Ожидание появления Главной страницы')
    def is_home_page_open(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.HOME_PAGE))
        return self.driver.find_element(*MainPageLocators.HOME_PAGE).is_displayed()

    @allure.title('Клик по лого Яндекс')
    def click_yandex_logo(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.YANDEX_LOGO)).click()

    @allure.title('Ожидание появления страницы Дзен')
    def is_dzen_page_open(self):
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.HOME_PAGE))
        return self.driver.find_element(*MainPageLocators.HOME_PAGE).is_displayed()
