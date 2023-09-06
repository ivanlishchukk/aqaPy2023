from hw_18.core_data.base_locators import BaseLocator


class HeaderLocators(BaseLocator):
    def __init__(self):
        super().__init__()
        self.logo = ("xpath", "//div[@class='header__logo']")