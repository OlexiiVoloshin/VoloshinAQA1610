from station_data import stations
from magic_methods import Train, TrainCar
from passenger_list import passengers_for_car1, passengers_for_car2


def main():
    # Створюємо вагони та додаємо пасажирів як раніше
    car1 = TrainCar(1, "пасажирський")
    car2 = TrainCar(2, "пасажирський")

    for passenger in passengers_for_car1:
        car1.add_passenger(passenger)

    for passenger in passengers_for_car2:
        car2.add_passenger(passenger)

    # Створюємо поїзд та додаємо вагони
    train = Train("Поїзд Ластівка", 150)
    train.add_car(car1)
    train.add_car(car2)

    # Змінна для зберігання поточної станції
    current_station = 0

    # Цикл для руху станціями
    for station in stations:
        # Посадка пасажирів на поточній станції
        for passenger in station["board_passengers_car1"]:
            train.cars[0].add_passenger(passenger)
        for passenger in station["board_passengers_car2"]:
            train.cars[1].add_passenger(passenger)

        # Висаджування пасажирів на поточній станції
        for passenger in station["departing_passengers_car1"]:
            if passenger in train.cars[0].passengers:
                train.cars[0].passengers.remove(passenger)
        for passenger in station["departing_passengers_car2"]:
            if passenger in train.cars[1].passengers:
                train.cars[1].passengers.remove(passenger)

        # Виведення інформації про пасажирів на станції
        print(f"На станції {station['name']} зайшли на поїзд (вагон 1):")
        for passenger in station["board_passengers_car1"]:
            print(f"- {passenger.name}")
        print(f"На станції {station['name']} зайшли на поїзд (вагон 2):")
        for passenger in station["board_passengers_car2"]:
            print(f"- {passenger.name}")

        print(f"На станції {station['name']} вийшли из поезда (вагон 1):")
        for passenger in station["departing_passengers_car1"]:
            print(f"- {passenger.name}")
        print(f"На станції {station['name']} вийшли из поезда (вагон 2):")
        for passenger in station["departing_passengers_car2"]:
            print(f"- {passenger.name}")

        # Переходимо до наступної станції
        current_station += 1

    # Виведення інформації про поїзд після завершення подорожі
    print(train)


if __name__ == "__main__":
    main()
