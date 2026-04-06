"""Page Object для страницы калькулятора."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CalculatorPage(BasePage):
    """Класс для работы со страницей калькулятора."""

    DELAY_INPUT = (By.ID, "delay")
    BUTTON_7 = (By.XPATH, "//span[text()='7']")
    BUTTON_8 = (By.XPATH, "//span[text()='8']")
    BUTTON_PLUS = (By.XPATH, "//span[text()='+']")
    BUTTON_EQUALS = (By.XPATH, "//span[text()='=']")
    SCREEN_RESULT = (By.CLASS_NAME, "screen")

    def open(self):
        """
        Открыть страницу калькулятора.

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        super().open(url)
        return self

    def set_delay(self, seconds: int):
        """
        Установить задержку перед вычислением.

        Args:
            seconds: Количество секунд задержки

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.input_text(self.DELAY_INPUT, str(seconds))
        return self

    def click_button_7(self):
        """
        Нажать кнопку с цифрой 7.

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.BUTTON_7)
        return self

    def click_button_8(self):
        """
        Нажать кнопку с цифрой 8.

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.BUTTON_8)
        return self

    def click_button_plus(self):
        """
        Нажать кнопку операции сложения (+).

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.BUTTON_PLUS)
        return self

    def click_button_equals(self):
        """
        Нажать кнопку равно (=).

        Returns:
            CalculatorPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.BUTTON_EQUALS)
        return self

    def get_result(self, timeout: int = 50) -> str:
        """
        Получить результат вычисления.

        Args:
            timeout: Время ожидания результата в секундах

        Returns:
            str: Результат вычисления
        """
        self.wait_for_text(self.SCREEN_RESULT, "15", timeout)
        return self.get_text(self.SCREEN_RESULT, timeout)