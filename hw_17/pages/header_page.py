from hw_17.pages.base_page import BasePage


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_logo_exist(self):
        locator = ("xpath", "//div[@class='header__logo']")
        element = self.wait_until_element_appears(locator)
        mouse_click = self.mouse_click(locator)

    def click_on_compare_items_button(self):
        locator = ("xpath", "//div[@class='header__icon --compare']")
        element = self.wait_until_element_appears(locator)
        mouse_click = self.mouse_click(locator)

    def assert_compare_button_works(self):
        locator = ("xpath", "//h1")
        element = self.wait_until_element_appears(locator)
        assert element.text == "Порівняння товарів"

    def click_on_empty_basket_button(self):
        locator = ("xpath", "//span[@id='cart']//span[@class='icon-counter__icon']//*[name()='svg']")
        element = self.wait_until_element_appears(locator)
        mouse_click = self.mouse_click(locator)

    def assert_basket_is_empty(self):
        locator = ("xpath", "//p[@class='text-center']")
        element = self.wait_until_element_appears(locator)
        assert element.text == "В кошику порожньо!"

    def go_to_login_page(self):
        locator = ("xpath", "//span[@id='open-login-modal']")
        element = self.wait_until_element_appears(locator)
        mouse_click = self.mouse_click(locator)

    def assert_login_page(self):
        locator = ("xpath", "//div[@class='modal-window__title']")
        element = self.wait_until_element_appears(locator)
        assert element.text == "Авторизація"

    def search_item(self, item_name):
        locator = ("xpath", "//input[@placeholder='Пошук товару по каталогу']")
        element = self.wait_until_element_appears(locator)
        element.send_keys(item_name)

    def assert_search_item(self):
        locator = ("xpath", "//div[@class='search-name'][1]")
        element = self.wait_until_element_appears(locator)
        assert element.text == 'FENDER AMERICAN PERFORMER STRATOCASTER MN SATIN LAKE PLACID BLUE Електрогітара'

    def change_language(self):
        locator = ("xpath", "//button[contains(text(),'Рус')]")
        element = self.wait_until_element_appears(locator)
        mouse_click = self.mouse_click(locator)

    def assert_language_changed(self):
        locator = ("xpath", "//div[@class='header__languages']")
        element = self.wait_until_element_appears(locator)
        assert element.text == 'Укр'