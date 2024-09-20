import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    @allure.title("Инициализация драйвера и WebDriverWait с заданным таймаутом")
    def __init__(self, driver, timeout=20):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    @allure.title("Поиск элемента с ожиданием, пока он не станет видимым")
    def find_element(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.title("Ожидание и клик по элементу")
    def click_element(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.title("Клик по элементу используя js скрипт")
    def click_element_script(self,question_locator):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(question_locator)
        )
        self.driver.execute_script("arguments[0].click();", button)

    @allure.title("Ожидание элемента, очистка поля и ввод текста")
    def input_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.title("Ожидание и проверка, что элемент отображается")
    def is_element_displayed(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.is_displayed()

    @allure.title("Ожидание, что элемент станет кликабельным")
    def wait_until_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    @allure.title("Ожидание, что элемент станет видимым")
    def wait_until_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
