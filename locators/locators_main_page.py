from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_PAGES = (By.XPATH, 'Header_Nav__AGCXC')
    ORDER_BUTTON_1 = (By.XPATH, '//button[@class="Button_Button__ra12g" and text()= "Заказать"]')
    ORDER_BUTTON_2 = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()= "Заказать"]')
    SAMOKAT_LOGO = (By.CSS_SELECTOR, 'a[href="/"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, 'a[href="//yandex.ru"]')

    HOME_PAGE = (By.CLASS_NAME, "Home_HomePage__ZXKIX")
    DZEN_PAGE = (By.CLASS_NAME, "zen-page _browser-name_firefox dzen-desktop--page-template__morda-1j _theme_white Theme_color_light Theme_root_light")
