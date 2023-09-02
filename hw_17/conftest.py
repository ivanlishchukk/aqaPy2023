from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from hw_17.pages.header_page import Header
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://muztorg.ua/uk/')

    yield driver
    driver.close()


@pytest.fixture
def header(driver):
    driver.get('https://muztorg.ua/uk/')

    yield Header(driver)