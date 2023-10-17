class TrainCar:
    def __init__(self, number, type):
        self.number = number  # Номер вагона
        self.type = type  # Тип вагона (наприклад, "пасажирський", "вантажний", тощо)
        self.passengers = []  # Список пасажирів у вагоні, спочатку порожній

    def add_passenger(self, passenger):
        if len(self.passengers) < 100:
            self.passengers.append(passenger)
        else:
            print(f"Вагон {self.number} заповнен. Не можна додати більше пасажирів.")

    def __len__(self):
        return len(self.passengers)

    def __str__(self):
        car_info = f'"traincart" :"{self.number}"\n'
        for passenger in self.passengers:
            car_info += f'"passanger_name": "{passenger.name}",\n"destination": "{passenger.destination}",\n"place": {passenger.place}\n'
        return car_info


class Train:
    def __init__(self, name, max_speed):
        self.name = name  # Назва поїзда
        self.max_speed = max_speed  # Максимальная швидкість поїзда
        self.cars = []  # Список вагонів, спочатку порожній

    def add_car(self, car):
        if isinstance(car, TrainCar):
            self.cars.append(car)
            print(f"Вагон {car.number} додан к поїзду {self.name}")
        else:
            print("Помилка: Можна додавати лише об'єкти типу TrainCar до поїзда")

    def __len__(self):
        # Повертаємо кількість вагонів (без локомотива)
        return len(self.cars)

    def __str__(self):
        return f"Поїзд {self.name}, Максимальная швідкість: {self.max_speed} км/ч, Кількість вагонів: {len(self)}"
