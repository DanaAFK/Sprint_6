import allure
from page_object.main_page import MainPage
from data import Data


class TestSamokatLogo:
    driver = None

    @allure.title('Проверка перехода на главную страницу по клику на лого Самокат ')
    @allure.description('Открываем главную страницу,Для наглядносьти,переход на другую страницу, Клик по логотипу "Самокат",Ожидание и проверка, что главная страница открылась')
    def test_click_to_logo(self, setup_driver):
        setup_driver.get(Data.URL)
        main_page = MainPage(setup_driver)

        main_page.click_order_button(1)
        main_page.click_samokat_logo()

        assert main_page.is_home_page_open()
