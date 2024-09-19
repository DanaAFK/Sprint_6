from selenium.webdriver.common.by import By


class OrderFormLocators:
    NAME_FIELD = (By.XPATH, '//input[@placeholder="* Имя"]')
    SURNAME_FIELD = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    ADDRESS_FIELD = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    METRO_FIELD = (By.XPATH, '//input[@class="select-search__input" and @placeholder="* Станция метро"]')
    METRO_ROKOSSOVSKOGO = (By.XPATH, '//div[text()="Бульвар Рокоссовского"]')
    PHONE_FIELD = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')
    FURTHER_BUTTON = (By.XPATH, "//button[text()='Далее']")