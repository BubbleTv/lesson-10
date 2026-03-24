"""Базовый класс для всех Page Object страниц."""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import allure


class BasePage:
    """Базовый класс, содержащий общие методы для всех страниц."""
    
    def __init__(self, driver: WebDriver):
        """
        Инициализация базовой страницы.
        
        Args:
            driver: Экземпляр WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def open(self, url: str):
        """
        Открыть указанный URL.
        
        Args:
            url: Адрес страницы для открытия
            
        Returns:
            BasePage: Возвращает экземпляр страницы для цепочки вызовов
        """
        self.driver.get(url)
        return self
    
    def find_element(self, locator: tuple, timeout: int = 10):
        """
        Найти элемент с ожиданием его видимости.
        
        Args:
            locator: Кортеж (By, selector)
            timeout: Время ожидания в секундах
            
        Returns:
            WebElement: Найденный элемент
        """
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
    
    def click_element(self, locator: tuple, timeout: int = 10):
        """
        Кликнуть по элементу.
        
        Args:
            locator: Кортеж (By, selector)
            timeout: Время ожидания в секундах
            
        Returns:
            BasePage: Возвращает экземпляр страницы для цепочки вызовов
        """
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()
        return self
    
    def input_text(self, locator: tuple, text: str, timeout: int = 10):
        """
        Ввести текст в поле ввода.
        
        Args:
            locator: Кортеж (By, selector)
            text: Текст для ввода
            timeout: Время ожидания в секундах
            
        Returns:
            BasePage: Возвращает экземпляр страницы для цепочки вызовов
        """
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)
        return self
    
