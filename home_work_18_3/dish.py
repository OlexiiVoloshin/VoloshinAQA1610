from abc import ABC, abstractmethod


class Dish(ABC):
    def __init__(self, name, price):
        """
        Конструктор класу Dish.

        :param name: Назва блюда або напою
        :param price: Ціна блюда або напою в гривнях
        """
        self.name = name
        self.price = price

    @abstractmethod
    def description(self):
        """
        Абстрактний метод для отримання опису блюда або напою.
        """
        pass


class HotDish(Dish):
    def __init__(self, name, price):
        """
        Конструктор класу HotDish, що наслідується від Dish.

        :param name: Назва гарячого блюда
        :param price: Ціна гарячого блюда в гривнях
        """
        super().__init__(name, price)

    def description(self):
        return f"{self.name} (Гаряче блюдо)"


class ColdDish(Dish):
    def __init__(self, name, price):
        """
        Конструктор класу ColdDish, що наслідується від Dish.

        :param name: Назва холодного блюда
        :param price: Ціна холодного блюда в гривнях
        """
        super().__init__(name, price)

    def description(self):
        return f"{self.name} (Холодне блюдо)"


class Drink(Dish):
    def __init__(self, name, price, is_alcoholic=False):
        """
        Конструктор класу Drink, що наслідується від Dish.

        :param name: Назва напою
        :param price: Ціна напою в гривнях
        :param is_alcoholic: Позначка, чи є напій алкогольним
        """
        super().__init__(name, price)
        self.is_alcoholic = is_alcoholic

    def description(self):
        if self.is_alcoholic:
            return f"{self.name} (Алкогольний напій)"
        else:
            return f"{self.name} (Безалкогольний напій)"
