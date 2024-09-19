import allure
import pytest
from selenium import webdriver
from page_object.about_rent import AboutRent
from page_object.main_page import MainPage
from page_object.order_form import OrderForm
from page_object.order_information import OrderInformation
from page_object.order_modal import OrderModal
from data import Data


class TestOrders:
    driver = None

    @allure.title('Открываем Браузер Firefox')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка бронирования самоката для двух кнопок "Заказать" на главной странице, через 2 набора данных')
    @allure.description('"Заказать",Заполнение формы заказа,Заполнение информации про аренду,Подтверждение заказа,Проверка, что заказ оформлен,Проверка, что информация о заказе отображается')
    @pytest.mark.parametrize("name, surname, address, phone, rent_date", [
        ("Дана", "Красивая", "Рубинштейна 13", "12345678901", "12.12.24"),
        ("Анна", "Иванова", "Ленина 25", "09876543210", "25.12.24")
    ])
    def test_order_scooter(self, name, surname, address, phone, rent_date):
        self.driver.get(Data.URL)
        main_page = MainPage(self.driver)
        main_page.click_order_button(1)

        order_form = OrderForm(self.driver)
        order_form.fill_order_form(name, surname, address, phone)
        order_form.click_further()

        about_rent = AboutRent(self.driver)
        about_rent.fill_rent_details(rent_date)
        about_rent.click_order()

        order_modal = OrderModal(self.driver)
        order_modal.confirm_order()

        assert order_modal.is_order_confirmed()
        order_modal. look_order_information()

        order_info = OrderInformation(self.driver)
        assert order_info.is_order_info_displayed()


    @allure.title('Закрытие драйвера')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()