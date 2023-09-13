import time
from hw_18.conftest import header, driver


def test_go_to_login(header):
    header.go_to_login_page()
    header.assert_login_page()
    time.sleep(3)


def test_search_item(header):
    header.search_item('Fender American')
    header.assert_search_item()
    time.sleep(3)


def test_click_on_empty_basket(header):
    header.click_on_empty_basket_button()
    header.assert_basket_is_empty()
    time.sleep(3)


def test_logo_exists(header):
    header.check_logo_exist()
    time.sleep(3)


def test_compare_items(header):
    header.click_on_compare_items_button()
    header.assert_compare_button_works()
    time.sleep(3)


def test_language_change(header):
    header.change_language()
    header.assert_language_changed()
    time.sleep(3)


def test_login(header):
    header.login_user()
    time.sleep(10)