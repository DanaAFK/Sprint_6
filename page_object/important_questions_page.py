import allure
from page_object.base_page import BasePage
from locators.locator_important_questions import ImportantQuestionsLocators


class ImportantQuestions(BasePage):

    @allure.step('Скролим страницу до формы вопросов')
    def scrolling_to_questions(self):
        subheader = self.find_element(ImportantQuestionsLocators.QUESTIONS)
        self.driver.execute_script("arguments[0].scrollIntoView();", subheader)

    @allure.step('Нажимаем на поле вопроса')
    def click_accordion_button(self, question_locator):
        self.click_element(question_locator)

    @allure.step('Ожидаем выпадающий список с определенным текстом')
    def get_accordion_panel_text(self, answer_locator):
        panel = self.find_element(answer_locator)
        return panel.text
