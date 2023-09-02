from hw_15.order import OrderFactory
import pytest


@pytest.fixture
def order_info():
    print('setup for test')
    yield OrderFactory('pizza', 'vegan')
    print('teardown for test')
