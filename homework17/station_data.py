from passenger_list import passengers_for_car1, passengers_for_car2

# Створюємо структуру даних для визначення станцій та пасажирів
stations = [
    {
        "name": "Станція Весела",
        "board_passengers_car1": [passengers_for_car1[0]],
        "departing_passengers_car1": [],
        "board_passengers_car2": [passengers_for_car2[0]],
        "departing_passengers_car2": [],
    },
    {
        "name": "Станція Шкільна",
        "board_passengers_car1": [passengers_for_car1[1]],
        "departing_passengers_car1": [passengers_for_car1[0]],
        "board_passengers_car2": [passengers_for_car2[1]],
        "departing_passengers_car2": [passengers_for_car2[0]],
    },
    {
        "name": "Станція Чудова",
        "board_passengers_car1": [passengers_for_car1[2]],
        "departing_passengers_car1": [passengers_for_car1[1]],
        "board_passengers_car2": [passengers_for_car2[2]],
        "departing_passengers_car2": [passengers_for_car2[1]],
    },
    {
        "name": "Станція Студентська",
        "board_passengers_car1": [passengers_for_car1[3]],
        "departing_passengers_car1": [passengers_for_car1[2]],
        "board_passengers_car2": [passengers_for_car2[3]],
        "departing_passengers_car2": [passengers_for_car2[2]],
    },
    {
        "name": "Станція Сонячна",
        "board_passengers_car1": [passengers_for_car1[4]],
        "departing_passengers_car1": [passengers_for_car1[3]],
        "board_passengers_car2": [passengers_for_car2[4]],
        "departing_passengers_car2": [passengers_for_car2[3]],
    },
    {
        "name": "Станція Місячна",
        "board_passengers_car1": [passengers_for_car1[5]],
        "departing_passengers_car1": [passengers_for_car1[4]],
        "board_passengers_car2": [passengers_for_car2[5]],
        "departing_passengers_car2": [passengers_for_car2[4]],
    },
    {
        "name": "Станція Розважальна",
        "board_passengers_car1": [passengers_for_car1[6]],
        "departing_passengers_car1": [passengers_for_car1[5]],
        "board_passengers_car2": [passengers_for_car2[6]],
        "departing_passengers_car2": [passengers_for_car2[5]],
    },
    {
        "name": "Станція Курортна",
        "board_passengers_car1": [passengers_for_car1[7]],
        "departing_passengers_car1": [passengers_for_car1[6]],
        "board_passengers_car2": [passengers_for_car2[7]],
        "departing_passengers_car2": [passengers_for_car2[6]],
    },
    {
        "name": "Станція Заводська",
        "board_passengers_car1": [passengers_for_car1[8]],
        "departing_passengers_car1": [passengers_for_car1[7]],
        "board_passengers_car2": [passengers_for_car2[8]],
        "departing_passengers_car2": [passengers_for_car2[7]],
    },
    {
        "name": "Станція Домашня",
        "board_passengers_car1": [passengers_for_car1[9]],
        "departing_passengers_car1": [passengers_for_car1[8]],
        "board_passengers_car2": [passengers_for_car2[9]],
        "departing_passengers_car2": [passengers_for_car2[8]],
    },
]
