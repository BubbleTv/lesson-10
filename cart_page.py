"""Page Object для страницы корзины."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class CartPage(BasePage):
    """Класс для работы со страницей корзины."""
    
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    
    def get_cart_items_count(self) -> int:
        """
        Получить количество товаров в корзине.
        
        Returns:
            int: Количество товаров в корзине
        """
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)
    
    def click_checkout(self):
        """
        Нажать кнопку Checkout для оформления заказа.
        
        Returns:
            CartPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.CHECKOUT_BUTTON)
        return self