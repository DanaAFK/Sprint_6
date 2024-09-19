import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locator_important_questions import ImportantQuestionsLocators


class ImportantQuestions:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Скролим страницу до формы вопросов')
    def scrolling_to_questions(self):
        subheader = self.driver.find_element(*ImportantQuestionsLocators.QUESTIONS)
        self.driver.execute_script("arguments[0].scrollIntoView();", subheader)

    @allure.step('Нажимаем на поле вопроса')
    def click_accordion_button(self, question_locator):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(question_locator)
        )
        self.driver.execute_script("arguments[0].click();", button)

    @allure.step('Ожидаем выпадающий список с определенным текстом')
    def get_accordion_panel_text(self, answer_locator):
        panel = WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(answer_locator)
        )
        return panel.text