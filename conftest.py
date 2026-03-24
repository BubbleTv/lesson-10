"""Фикстуры для pytest."""

import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    """Фикстура для создания Chrome WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def firefox_driver():
    """Фикстура для создания Firefox WebDriver."""
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()