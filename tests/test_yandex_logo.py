import allure
from page_object.main_page import MainPage
from data import Data


class TestYandexLogo:
    driver = None

    @allure.title('Проверка перехода на страницу Дзен по клику на лого Яндекс')
    @allure.description('Открываем главную страницу,Клик по логотипу "Яндекс",Ожидание и проверка, что страница Дзен открылась')
    def test_click_to_logo(self, setup_driver):
        setup_driver.get(Data.URL)
        main_page = MainPage(setup_driver)

        main_page.click_yandex_logo()

        assert main_page.is_dzen_page_open()
