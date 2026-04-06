"""Page Object для главной страницы магазина."""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import allure


class InventoryPage(BasePage):
    """Класс для работы с главной страницей магазина."""

    BACKPACK_BUTTON = (By.ID, "add-to-cart-sauce-labs-backpack")
    BOLT_TSHIRT_BUTTON = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.ID, "add-to-cart-sauce-labs-onesie")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")

    def add_backpack_to_cart(self):
        """
        Добавить рюкзак Sauce Labs Backpack в корзину.

        Returns:
            InventoryPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.BACKPACK_BUTTON)
        return self

    def add_bolt_tshirt_to_cart(self):
        """
        Добавить футболку Sauce Labs Bolt T-Shirt в корзину.

        Returns:
            InventoryPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.BOLT_TSHIRT_BUTTON)
        return self

    def add_onesie_to_cart(self):
        """
        Добавить товар Sauce Labs Onesie в корзину.

        Returns:
            InventoryPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.ONESIE_BUTTON)
        return self

    def go_to_cart(self):
        """
        Перейти в корзину.

        Returns:
            InventoryPage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.click_element(self.CART_ICON)
        return self