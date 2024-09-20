from selenium.webdriver.common.by import By


class OrderModalLocators:
    CONFIRM_MODAL = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    CONFIRM_YES_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button__") and contains(@class, "Button_Middle__") and text()="Да"]')

    ORDER_MODAL = (By.XPATH, '//div[contains(@class, "Order_ModalHeader") and text()="Заказ оформлен"]')
    LOOK_ORDER_INFO_BUTTON = (By.XPATH, '//button[contains(@class, "Button_Button") and contains(@class, "Button_Middle") and text()="Посмотреть статус"]')