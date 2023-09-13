from selenium.webdriver import Chrome
from selenium.webdriver.support.wait import WebDriverWait
from hw_18.pages.header_page import Header
from hw_18.pages.category_page import CategoryPage
import pytest


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()
    driver.get('https://muztorg.ua/uk/')
    driver.get_cookie('flag')
    driver.add_cookie({'name':'flag', 'value':'red'})

    yield driver
    driver.close()


@pytest.fixture
def header(driver):
    driver.get('https://muztorg.ua/uk/')

    yield Header(driver)

@pytest.fixture
def categories(driver):
    driver.get("https://muztorg.ua/uk/gitari/")
    driver.maximize_window()

    yield CategoryPage(driver)