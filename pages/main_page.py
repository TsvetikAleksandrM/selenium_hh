from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constants import Constants as Const
import time


class MainPage:
    """
    Класс для работы с главной страницей
    """

    def __init__(self, driver):
        self.driver = driver

    def open_page(self):
        """
        Открыть страницу hh.ru
        """
        self.driver.get(Const.HOST_NAME)

    def login(self):
        """
        Авторизация в системе
        """
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.LINK_TEXT, Const.BUTTON_ENTER))).click()
        time.sleep(3)
        input_login = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Const.INPUT_LOGIN_СSS)))
        input_login.clear()
        input_login.send_keys(Const.USER_NAME)
        input_password = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.NAME, Const.INPUT_PASSWORD_NAME)))
        input_password.clear()
        input_password.send_keys(Const.USER_PASSWORD)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, Const.BUTTON_ENTER_OFFICE))).click()