from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_PAGES = (By.XPATH, '//div[contains(@class, "Header_Nav")]')
    ORDER_BUTTON_1 = (By.XPATH, '//button[contains(@class,"Button_Button__") and text()= "Заказать"]')
    ORDER_BUTTON_2 = (By.XPATH, '//button[contains(@class, "Button_Button__") and contains(@class, "Button_Middle__") and text()= "Заказать"]')
    SAMOKAT_LOGO = (By.CSS_SELECTOR, 'a[href="/"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[href="//yandex.ru"]')

    HOME_PAGE = (By.XPATH, '//div[contains(@class, "Home_HomePage__")]')
    DZEN_PAGE = (By.CLASS_NAME, "zen-page _browser-name_firefox dzen-desktop--page-template__morda-1j _theme_white Theme_color_light Theme_root_light")
