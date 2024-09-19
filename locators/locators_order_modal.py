from selenium.webdriver.common.by import By


class OrderModalLocators:
    CONFIRM_MODAL = (By.XPATH, '//div[text()="Хотите оформить заказ?"]')
    CONFIRM_YES_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Да"]')

    ORDER_MODAL = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ" and text()="Заказ оформлен"]')
    LOOK_ORDER_INFO_BUTTON = (By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM" and text()="Посмотреть статус"]')