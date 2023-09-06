from hw_18.pages.base_page import BasePage
from hw_18.pages.category_page import CategoryPage
from hw_18.core_data.header_locators import HeaderLocators
from hw_18.core_data.categories_locators import CategoriesLocator

class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locator = HeaderLocators()
        self.locator_cat = CategoriesLocator()

    def go_to_guitar_cat(self):
        self.mouse_click(self.locator_cat.guitars)
        return CategoryPage(self._driver)

    def check_logo_exist(self):
        element = self.wait_until_element_appears(self.locator.logo)
        mouse_click = self.mouse_click(self.locator.logo)

    def click_on_compare_items_button(self):
        element = self.wait_until_element_appears(self.locator.compare)
        mouse_click = self.mouse_click(self.locator.compare)

    def assert_compare_button_works(self):
        element = self.wait_until_element_appears(self.locator.compare_conf)
        assert element.text == "Порівняння товарів"

    def click_on_empty_basket_button(self):
        element = self.wait_until_element_appears(self.locator.basket)
        mouse_click = self.mouse_click(self.locator.basket)

    def assert_basket_is_empty(self):
        element = self.wait_until_element_appears(self.locator.basket_conf)
        assert element.text == "В кошику порожньо!"

    def go_to_login_page(self):
        element = self.wait_until_element_appears(self.locator.login)
        mouse_click = self.mouse_click(self.locator.login)

    def assert_login_page(self):
        element = self.wait_until_element_appears(self.locator.modal)
        assert element.text == "Авторизація"

    def search_item(self, item_name):
        element = self.wait_until_element_appears(self.locator.search_field)
        element.send_keys(item_name)

    def assert_search_item(self):
        element = self.wait_until_element_appears(self.locator.search_field_conf)
        assert element.text == 'FENDER AMERICAN PERFORMER STRATOCASTER MN SATIN LAKE PLACID BLUE Електрогітара'

    def change_language(self):
        element = self.wait_until_element_appears(self.locator.language)
        mouse_click = self.mouse_click(self.locator.language)

    def assert_language_changed(self):
        element = self.wait_until_element_appears(self.locator.language_conf)
        assert element.text == 'Укр'