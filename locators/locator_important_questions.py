from selenium.webdriver.common.by import By


class ImportantQuestionsLocators:

    QUESTIONS = (By.CLASS_NAME, 'accordion')

    QUESTION_1_BUTTON = [By.XPATH, '//*[@id="accordion__heading-0"]']
    QUESTION_2_BUTTON = [By.XPATH, '//*[@id="accordion__heading-1"]']
    QUESTION_3_BUTTON = [By.XPATH, '//*[@id="accordion__heading-2"]']
    QUESTION_4_BUTTON = [By.XPATH, '//*[@id="accordion__heading-3"]']
    QUESTION_5_BUTTON = [By.XPATH, '//*[@id="accordion__heading-4"]']
    QUESTION_6_BUTTON = [By.XPATH, '//*[@id="accordion__heading-5"]']
    QUESTION_7_BUTTON = [By.XPATH, '//*[@id="accordion__heading-6"]']
    QUESTION_8_BUTTON = [By.XPATH, '//*[@id="accordion__heading-7"]']

    ANSWER_1_PANEL = [By.XPATH, '//*[@id="accordion__panel-0"]']
    ANSWER_2_PANEL = [By.XPATH, '//*[@id="accordion__panel-1"]']
    ANSWER_3_PANEL = [By.XPATH, '//*[@id="accordion__panel-2"]']
    ANSWER_4_PANEL = [By.XPATH, '//*[@id="accordion__panel-3"]']
    ANSWER_5_PANEL = [By.XPATH, '//*[@id="accordion__panel-4"]']
    ANSWER_6_PANEL = [By.XPATH, '//*[@id="accordion__panel-5"]']
    ANSWER_7_PANEL = [By.XPATH, '//*[@id="accordion__panel-6"]']
    ANSWER_8_PANEL = [By.XPATH, '//*[@id="accordion__panel-7"]']

    ANSWER_1_PANEL_TEXT = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
    ANSWER_2_PANEL_TEXT = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
    ANSWER_3_PANEL_TEXT = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
    ANSWER_4_PANEL_TEXT = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
    ANSWER_5_PANEL_TEXT = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
    ANSWER_6_PANEL_TEXT = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
    ANSWER_7_PANEL_TEXT = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
    ANSWER_8_PANEL_TEXT = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'