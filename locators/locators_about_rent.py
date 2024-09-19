from selenium.webdriver.common.by import By


class AboutRentLocators:
    RENT_DATE = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    RENT_PERIOD_FIELD = (By.CLASS_NAME, "Dropdown-arrow")
    RENT_PERIOD_TWO_DAYS = (By.XPATH, '//div[@class="Dropdown-option" and text()="двое суток"]')
    COLOR_BLACK_CHECKBOX = (By.XPATH, '//label[text()="чёрный жемчуг"]')
    ORDER_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Заказать"]')