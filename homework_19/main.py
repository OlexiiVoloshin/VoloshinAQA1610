from passenger_list import passengers_for_car1, passengers_for_car2
from magic_methods import Train, TrainCar


def main():
    # Створюємо вагони та додаємо пасажирів

    car1 = TrainCar(1, "пасажирській")
    car2 = TrainCar(2, "пасажирській")

    for passenger in passengers_for_car1:
        car1.add_passenger(passenger)

    for passenger in passengers_for_car2:
        car2.add_passenger(passenger)

    # Створюємо потяг та додаємо вагони
    train = Train("Поїзд Ластівка", 150)
    train.add_car(car1)
    train.add_car(car2)

    # Вивід інформації про поїзд, вагони і пасажирів з використанням __str__
    print(train)  # Вивід інформації про поїзд
    for car in train.cars:
        print(car)  # Вивід інформації про вагони
        for passenger in car.passengers:
            print(passenger)  # Вивід інформації про пасажирів в вагоні

    # Вивід кількості пасажирів в вагоні при використанні функції len
    print(f"Кількість пасажирів в першому вагоні: {len(car1)}")
    print(f"Кількість пасажирів в другому вагоні: {len(car2)}")


if __name__ == "__main__":
    main()
