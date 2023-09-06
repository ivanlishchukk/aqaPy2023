from hw_18.core_data.base_locators import BaseLocator


class CategoriesLocator(BaseLocator):
    def __init__(self):
        super().__init__()
        self.guitars = ("xpath", "//a[@class='category__link'][contains(text(),'Гітари')]")
        self.results = ("xpath", "(//div[@class='caption'])[1]")