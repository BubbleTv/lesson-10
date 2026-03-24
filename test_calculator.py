"""Тесты для проверки калькулятора."""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure
from pages.calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.story("Проверка работы калькулятора с задержкой")
@allure.title("Тест вычисления 7 + 8 с задержкой 45 секунд")
@allure.description("""
    Тест проверяет, что калькулятор корректно вычисляет сумму 7 + 8 
    при установленной задержке 45 секунд.
    
    Шаги:
    1. Открыть страницу калькулятора
    2. Установить задержку 45 секунд
    3. Нажать кнопки 7, +, 8, =
    4. Дождаться результата
    5. Проверить, что результат равен 15
""")
@allure.severity(allure.severity_level.CRITICAL)
class TestCalculator:
    
    @allure.title("Проверка вычисления 7 + 8")
    def test_calculator_addition(self):
        """Тест проверки сложения 7 + 8."""
        chrome_options = Options()
        chrome_options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=chrome_options)
        
        try:
            with allure.step("Создание объекта страницы калькулятора"):
                calculator = CalculatorPage(driver)
            
            with allure.step("Открытие страницы калькулятора"):
                calculator.open()
            
            with allure.step("Установка задержки 45 секунд"):
                calculator.set_delay(45)
            
            with allure.step("Ввод выражения 7 + 8"):
                calculator.click_button_7()
                calculator.click_button_plus()
                calculator.click_button_8()
            
            with allure.step("Нажатие кнопки равно"):
                calculator.click_button_equals()
            
            with allure.step("Ожидание и получение результата"):
                result = calculator.get_result(timeout=50)
            
            with allure.step("Проверка результата вычисления"):
                assert result == "15", f"Ожидался результат '15', получен '{result}'"
                
        finally:
            with allure.step("Закрытие браузера"):
                driver.quit()