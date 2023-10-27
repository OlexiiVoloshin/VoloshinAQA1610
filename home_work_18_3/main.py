from dish import HotDish, ColdDish, Drink
from order import Order, OrderPart

# Створюємо блюда
pasta = HotDish("Паста", 150)
risotto = HotDish("Різотто", 180)
salad = ColdDish("Салат", 90)
cola = Drink("Кола", 25)
wine = Drink("Вино", 120, is_alcoholic=True)
steak = HotDish("Стейк", 250)
sushi = HotDish("Суші", 220)
ice_cream = ColdDish("Морозиво", 60)
coffee = Drink("Кава", 30)
cocktail = Drink("Коктейль", 70, is_alcoholic=True)

# Створюємо частини замовлення зі спеціальними вимогами
order_part1 = OrderPart(pasta, 2, "Без солі")
order_part2 = OrderPart(risotto, 1, "З грибами")
order_part3 = OrderPart(salad, 3, "Без олії")
order_part4 = OrderPart(cola, 4, "Льодом")
order_part5 = OrderPart(wine, 1, "Червоне")
order_part6 = OrderPart(steak, 2, "Medium-rare")
order_part7 = OrderPart(sushi, 2, "З імбирем")
order_part8 = OrderPart(ice_cream, 4, "Шоколадне")
order_part9 = OrderPart(coffee, 3, "З цукром")
order_part10 = OrderPart(cocktail, 2, "Без льоду")

# Створюємо замовлення
order = Order("2023-10-27 19:30")

# Додаємо частини замовлення до замовлення
order.add_item(order_part1)
order.add_item(order_part2)
order.add_item(order_part3)
order.add_item(order_part4)
order.add_item(order_part5)
order.add_item(order_part6)
order.add_item(order_part7)
order.add_item(order_part8)
order.add_item(order_part9)
order.add_item(order_part10)

# Виводимо інформацію про замовлення
print(f"Час замовлення: {order.order_time}")
order.list_items()
