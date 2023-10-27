class OrderPart:
    def __init__(self, dish, quantity, special_requests=None):
        """
        Конструктор класу OrderPart.

        :param dish: Об'єкт блюда або напою
        :param quantity: Кількість одиниць блюда або напою в замовленні
        :param special_requests: Спеціальні вимоги або коментарі до частини замовлення (за бажанням)
        """
        self.dish = dish
        self.quantity = quantity
        self.special_requests = special_requests if special_requests is not None else ""

    def set_special_requests(self, special_requests):
        """
        Встановлює спеціальні вимоги або коментарі для частини замовлення.

        :param special_requests: Спеціальні вимоги або коментарі до частини замовлення (за бажанням)
        """
        self.special_requests = special_requests

    def get_special_requests(self):
        """
        Отримує спеціальні вимоги або коментарі до частини замовлення.

        :return: Спеціальні вимоги або коментарі до частини замовлення
        """
        return self.special_requests


class Order:
    def __init__(self, order_time):
        """
        Конструктор класу Order.

        :param order_time: Час замовлення
        """
        self.order_time = order_time
        self.order_items = []

    def add_item(self, order_part):
        """
        Додає частину замовлення до замовлення.

        :param order_part: Частина замовлення (об'єкт класу OrderPart)
        """
        self.order_items.append(order_part)

    def total_price(self):
        """
        Розраховує загальну вартість замовлення.

        :return: Загальна вартість замовлення в гривнях
        """
        total = sum(order_part.dish.price * order_part.quantity for order_part in self.order_items)
        return total

    def list_items(self):
        """
        Виводить інформацію про частини замовлення та загальну вартість замовлення.
        """
        for order_part in self.order_items:
            description = f"{order_part.quantity} x {order_part.dish.description()}: {order_part.dish.price} грн"
            if order_part.get_special_requests():
                description += f" ({order_part.get_special_requests()})"
            print(description)
        print(f"Загальна вартість: {self.total_price()} грн")
