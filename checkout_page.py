"""Page Object для страницы оформления заказа."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CheckoutPage(BasePage):
    """Класс для работы со страницей оформления заказа."""
    
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполнить форму оформления заказа.
        
        Args:
            first_name: Имя покупателя
            last_name: Фамилия покупателя
            postal_code: Почтовый индекс
            
        Returns:
            CheckoutPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.input_text(self.FIRST_NAME_INPUT, first_name)
        self.input_text(self.LAST_NAME_INPUT, last_name)
        self.input_text(self.POSTAL_CODE_INPUT, postal_code)
        return self
    
    def click_continue(self):
        """
        Нажать кнопку Continue для перехода к подтверждению заказа.
        
        Returns:
            CheckoutPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.CONTINUE_BUTTON)
        return self
    
    def get_total(self) -> str:
        """
        Получить итоговую сумму заказа.
        
        Returns:
            str: Итоговая сумма (число без знака $)
        """
        total_text = self.get_text(self.TOTAL_LABEL)
        total_amount = total_text.split("$")[1]
        return total_amount