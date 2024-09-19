import allure
from selenium import webdriver
from page_object.important_questions_page import ImportantQuestions
from locators.locator_important_questions import ImportantQuestionsLocators
from data import Data


class TestImportantQuestions:
    driver = None

    @allure.title('Открываем Браузер Firefox')
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()

    @allure.title('Проверка выпадающего списка у первого вопроса')
    @allure.description('Скролим страницу до блока всопросами и проверяем клик по вопросу, аналогичные тесты далее')
    def test_accordion_button_question_1(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_1_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_1_PANEL)

        expected_answer = (ImportantQuestionsLocators.ANSWER_1_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у второго вопроса')
    def test_accordion_button_question_2(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_2_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_2_PANEL)

        expected_answer = (ImportantQuestionsLocators.ANSWER_2_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у третьего вопроса')
    def test_accordion_button_question_3(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_3_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_3_PANEL)

        expected_answer = (ImportantQuestionsLocators.ANSWER_3_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у четвертого вопроса')
    def test_accordion_button_question_4(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_4_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_4_PANEL)
        expected_answer = (ImportantQuestionsLocators.ANSWER_4_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у пятого вопроса')
    def test_accordion_button_question_5(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_5_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_5_PANEL)
        expected_answer = (ImportantQuestionsLocators.ANSWER_5_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у шестого вопроса')
    def test_accordion_button_question_6(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_6_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_6_PANEL)
        expected_answer = (ImportantQuestionsLocators.ANSWER_6_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у седьмого вопроса')
    def test_accordion_button_question_7(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_7_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_7_PANEL)
        expected_answer = (ImportantQuestionsLocators.ANSWER_7_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Проверка выпадающего списка у восьмого вопроса')
    def test_accordion_button_question_8(self):
        self.driver.get(Data.URL)
        important_question = ImportantQuestions(self.driver)

        important_question.scrolling_to_questions()
        important_question.click_accordion_button(ImportantQuestionsLocators.QUESTION_8_BUTTON)

        actual_answer = important_question.get_accordion_panel_text(ImportantQuestionsLocators.ANSWER_8_PANEL)
        expected_answer = (ImportantQuestionsLocators.ANSWER_8_PANEL_TEXT)
        assert actual_answer == expected_answer

    @allure.title('Закрытие драйвера')
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()