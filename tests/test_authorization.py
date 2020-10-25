from selenium import webdriver
from pages.main_page import MainPage
from pages.home_page import HomePage


class TestAuthorization:
    """
    Тесты авторизации
    """

    def setup_class(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\chromedriver.exe')
        self.driver.maximize_window()
        self.main_page = MainPage(self.driver)
        self.home_page = HomePage(self.driver)

    def test_authorization(self):
        """
        Тест авторизации
        """
        self.main_page.open_page()
        self.main_page.login()
        self.home_page.check_page()

    def teardown_class(self):
        """
        Закрыть браузер
        """
        self.driver.quit()
