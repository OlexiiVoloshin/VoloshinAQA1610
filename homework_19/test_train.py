import pytest
from magic_methods import TrainCar, Train
from passenger_list import passengers_for_car1, passengers_for_car2


# Фікстура, яка створює інстанс поїзда разом з вагонами та пасажирами для інших тестів
@pytest.fixture
def create_train_instance():
    """
    Ця фікстура створює інстанс поїзда з двома вагонами та пасажирами для інших тестів.
    """
    car1 = TrainCar(1, "пасажирський")
    car2 = TrainCar(2, "пасажирський")

    for passenger in passengers_for_car1:
        car1.add_passenger(passenger)

    for passenger in passengers_for_car2:
        car2.add_passenger(passenger)

    train = Train("Поїзд Ластівка", 150)
    train.add_car(car1)
    train.add_car(car2)

    return train


# Тест для перевірки створення вагону
@pytest.mark.smoke
def test_train_car_creation():
    """
    Цей тест перевіряє, чи коректно створюється вагон.
    Вагон повинен мати номер, тип та бути пустим без пасажирів.
    """
    car = TrainCar(1, "пасажирський")
    assert car.number == 1
    assert car.type == "пасажирський"
    assert len(car) == 0


# Тест для перевірки додавання пасажира в вагон
@pytest.mark.smoke
def test_train_car_add_passenger():
    """
    Цей тест перевіряє, чи коректно додається пасажир в вагон.
    Після додавання пасажира, вагон повинен містити одного пасажира.
    """
    car = TrainCar(1, "пасажирський")
    passenger = passengers_for_car1[0]
    car.add_passenger(passenger)
    assert len(car) == 1


# Тест для перевірки створення поїзда
@pytest.mark.smoke
def test_train_creation(create_train_instance):
    """
    Цей тест перевіряє, чи коректно створюється поїзд разом із вагонами та пасажирами.
    Поїзд повинен мати назву та максимальну швидкість.
    """
    train = create_train_instance
    assert train.name == "Поїзд Ластівка"
    assert train.max_speed == 150


# Тест для перевірки додавання вагону до поїзда
@pytest.mark.regression
def test_train_add_car(create_train_instance):
    """
    Цей тест перевіряє, чи коректно додається вагон до поїзда.
    Після додавання вагону, кількість вагонів у поїзді повинна збільшитися.
    """
    train = create_train_instance
    car = TrainCar(3, "пасажирський")
    train.add_car(car)
    assert len(train) == 3


# Тест для перевірки видалення вагону з поїзда
@pytest.mark.regression
def test_train_remove_car(create_train_instance):
    """
    Цей тест перевіряє, чи коректно видаляється вагон з поїзда.
    Після видалення вагону, кількість вагонів у поїзді повинна зменшитися.
    """
    train = create_train_instance
    car = train.cars[0]
    train.cars.remove(car)
    assert len(train) == 1


# Тест для перевірки створення пасажира
@pytest.mark.regression
def test_passenger_creation():
    """
    Цей тест перевіряє, чи коректно створюється пасажир.
    Пасажир повинен мати ім'я, номер білету, пункт призначення та номер місця.
    """
    passenger = passengers_for_car1[0]
    assert passenger.name == "John Dow"
    assert passenger.ticket_number == "12345"
    assert passenger.destination == "Station A"
    assert passenger.place == 1


# Параметризований тест для перевірки імен пасажирів
@pytest.mark.parametrize("passenger_index, expected_name", [(0, "John Dow"), (1, "Alex Dowson"), (2, "Lisa Smith")])
def test_passenger_names(passenger_index, expected_name):
    """
    Цей параметризований тест перевіряє імена пасажирів за допомогою індексу та очікуваних імен.
    """
    passenger = passengers_for_car1[passenger_index]
    assert passenger.name == expected_name


if __name__ == "__main__":
    pytest.main()
