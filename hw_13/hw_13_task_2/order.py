from dishes.pizza import Pizza
from dishes.risotto import Risotto
from dishes.pasta import Pasta


class OrderFactory:
    @staticmethod
    def get_dish(dish_type):
        if dish_type == 'pizza':
            return Pizza()
        elif dish_type == 'risotto':
            return Risotto()
        elif dish_type == 'pasta':
            return Pasta()


order_risotto = OrderFactory.get_dish('risotto')
print(order_risotto.get_dish('classic'))
order_pizza = OrderFactory.get_dish('pizza')
print(order_pizza.get_dish('vegan'))
order_pasta = OrderFactory.get_dish('pasta')
print(order_pasta.get_dish('carbonara'))
