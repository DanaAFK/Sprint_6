import allure
import pytest
from page_object.important_questions_page import ImportantQuestions
from locators.locator_important_questions import ImportantQuestionsLocators
from data import Data


@pytest.mark.usefixtures("setup_driver")
class TestImportantQuestions:
    driver = None

    @allure.title('Проверка выпадающего списка вопросов, Теперь с использованием параметризации')
    @allure.description('Скролим страницу до блока с вопросами и проверяем клик по каждому вопросу и правильность ответа.')
    @pytest.mark.parametrize("question_button_locator, answer_panel_locator, expected_answer_text", [
        (button, answer_panel, answer_text)
        for button, (answer_panel, answer_text) in ImportantQuestionsLocators.QUESTIONS_AND_ANSWERS.items()
    ])
    def test_accordion_button_question(self, setup_driver, question_button_locator, answer_panel_locator, expected_answer_text):
        setup_driver.get(Data.URL)
        important_question = ImportantQuestions(setup_driver)

        important_question.scrolling_to_questions()

        important_question.click_element_script(getattr(ImportantQuestionsLocators, question_button_locator))

        actual_answer = important_question.get_accordion_panel_text(answer_panel_locator)

        assert actual_answer == expected_answer_text
