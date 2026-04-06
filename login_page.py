"""Page Object для страницы авторизации."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class LoginPage(BasePage):
    """Класс для работы со страницей авторизации."""

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    def open(self):
        """
        Открыть страницу авторизации.

        Returns:
            LoginPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        url = "https://www.saucedemo.com/"
        super().open(url)
        return self

    def login(self, username: str, password: str):
        """
        Выполнить авторизацию.

        Args:
            username: Имя пользователя
            password: Пароль

        Returns:
            LoginPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.input_text(self.USERNAME_INPUT, username)
        self.input_text(self.PASSWORD_INPUT, password)
        self.click_element(self.LOGIN_BUTTON)
        return self