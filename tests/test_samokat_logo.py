import allure
from selenium import webdriver
from page_object.main_page import MainPage
from data import Data


class TestSamokatLogo:
    driver = None

    @allure.title('Открываем Браузер Firefox')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка перехода на главную страницу по клику на лого Самокат ')
    @allure.description('Открываем главную страницу,Для наглядносьти,переход на другую страницу, Клик по логотипу "Самокат",Ожидание и проверка, что главная страница открылась')
    def test_click_to_logo(self):
        self.driver.get(Data.URL)
        main_page = MainPage(self.driver)

        main_page.click_order_button(1)
        main_page.click_samokat_logo()

        assert main_page.is_home_page_open()

    @allure.title('Закрытие драйвера')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()