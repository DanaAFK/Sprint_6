from selenium.webdriver.common.by import By


class OrderInformationLocators:
    ORDER_STATUS_INFO = (By.XPATH, "//div[contains(@class,'Track_Content')]")
    