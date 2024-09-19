import allure
from selenium import webdriver
from page_object.main_page import MainPage
from data import Data


class TestYandexLogo:
    driver = None

    @allure.title('Открываем Браузер Firefox')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка перехода на страницу Дзен по клику на лого Яндекс')
    @allure.description('Открываем главную страницу,Клик по логотипу "Яндекс",Ожидание и проверка, что страница Дзен открылась')
    def test_click_to_logo(self):
        self.driver.get(Data.URL)
        main_page = MainPage(self.driver)

        main_page.click_yandex_logo()

        assert main_page.is_dzen_page_open()

    @allure.title('Закрытие драйвера')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()