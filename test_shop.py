"""Тесты для проверки интернет-магазина."""

import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import allure
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("Интернет-магазин")
@allure.story("Оформление заказа")
@allure.title("Тест оформления заказа с проверкой итоговой суммы")
@allure.description("""
    Тест проверяет полный сценарий оформления заказа:
    1. Авторизация пользователя standard_user
    2. Добавление трех товаров в корзину
    3. Переход в корзину и оформление заказа
    4. Заполнение формы данными
    5. Проверка итоговой суммы заказа

    Ожидаемый результат: итоговая сумма равна $58.29
""")
@allure.severity(allure.severity_level.BLOCKER)
class TestShop:

    @allure.title("Проверка оформления заказа")
    def test_shop_checkout(self):
        """Тест оформления заказа в интернет-магазине."""
        firefox_options = Options()
        firefox_options.add_argument("--start-maximized")
        driver = webdriver.Firefox(options=firefox_options)

        try:
            with allure.step("Создание объектов страниц"):
                login_page = LoginPage(driver)
                inventory_page = InventoryPage(driver)
                cart_page = CartPage(driver)
                checkout_page = CheckoutPage(driver)

            with allure.step("Авторизация пользователя standard_user"):
                login_page.open()
                login_page.login("standard_user", "secret_sauce")

            with allure.step("Добавление товаров в корзину"):
                inventory_page.add_backpack_to_cart()
                inventory_page.add_bolt_tshirt_to_cart()
                inventory_page.add_onesie_to_cart()

            with allure.step("Переход в корзину"):
                inventory_page.go_to_cart()

            with allure.step("Нажатие кнопки Checkout"):
                cart_page.click_checkout()

            with allure.step("Заполнение формы данными"):
                checkout_page.fill_checkout_form("Иван", "Петров", "123456")

            with allure.step("Нажатие кнопки Continue"):
                checkout_page.click_continue()

            with allure.step("Получение итоговой суммы"):
                total = checkout_page.get_total()

            with allure.step("Проверка итоговой суммы"):
                expected_total = "58.29"
                assert total == expected_total, (
                    f"Ожидалась сумма '{expected_total}', получена '{total}'"
                )

        finally:
            with allure.step("Закрытие браузера"):
                driver.quit()