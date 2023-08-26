from hw_15.fixturecode import order_info
import pytest


@pytest.mark.run
def test_change_dish_type(order_info):
    order_info.change_dish_type('pasta')
    assert order_info.dish_type == 'pasta'


@pytest.mark.to_do
@pytest.mark.xfail(reason='failed due test is not ready')
def test_change_dish_option(order_info):
    order_info.change_dish_option('carbonara')
    assert order_info.dish_option == 'carbonara'


@pytest.mark.skip
@pytest.mark.to_fix
def test_change_order(order_info):
    order_info.change_dish_type('pizza')
    assert order_info.dish_type == 'pasta'


@pytest.mark.parametrize(
    "d_type,expected", [('pasta','pasta'),('risotto','risoto')] #positive|negative tests :_
)
def test_change_dish_type2(order_info, d_type, expected):
    order_info.change_dish_type(d_type)
    assert order_info.dish_type == expected