from selenium.webdriver.common.by import By
from constants.constants import Constants as Const


class HomePage:
    """
    Класс для работы с домашней страницей
    """

    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        """
        Проверка нахождения на странице
        """
        element = self.driver.find_element(By.CSS_SELECTOR, Const.INPUT_ELEMENT_CSS)
        element.is_displayed()
        assert element, "Element not found"
