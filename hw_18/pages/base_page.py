import selenium.webdriver
import pickle
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)

    def wait_until_element_appears(self, locator):
        return self.__web_driver_wait.until(EC.presence_of_element_located(locator))

    def mouse_click(self, locator):
        self.wait_until_element_appears(locator).click()

    def send_keys_to_field(self, locator, text):
        self.wait_until_element_appears(locator).send_keys(text)


class Cookies:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)

    def get_cookie(self, driver):
        pickle.dump(driver.get_cookies(), open("cookies.pkl", "wb"))

    def set_cookies(self, driver):
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            driver.add_cookie(cookie)


class LocalStorage:
    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)

    def set_local_storage(self, driver):
        driver.execute_script("window.localStorage.setItem('key','value');")

    def get_local_storage(selfself, driver):
        driver.execute_script("window.localStorage.getItem('key');")
