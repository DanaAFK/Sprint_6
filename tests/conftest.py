import allure
import pytest
from selenium import webdriver


@allure.title('Фикстура для инициализации и закрытия браузера')
@allure.description('Фикстура будет инициализировать браузер и закрывать его после завершения тестов')
@pytest.fixture(scope="class")
def setup_driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()
