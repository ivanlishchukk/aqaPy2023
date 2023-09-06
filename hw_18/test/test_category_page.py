import time
from hw_18.conftest import header, driver


def test_go_to_first_result(header):
    category_page = header.go_to_guitar_cat()
    product_page = category_page.go_to_first_result()
    time.sleep(5)

