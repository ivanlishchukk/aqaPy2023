from hw_18.pages.base_page import BasePage
from hw_18.pages.product_page import ProductPage
from hw_18.core_data.categories_locators import CategoriesLocator


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoriesLocator()

    def go_to_first_result(self):
        self.mouse_click(self.locators.results)
        return ProductPage(self._driver)

    def filter_new(self):
        self.mouse_click(self.locators.guitars)
