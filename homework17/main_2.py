from datetime import datetime


def calculate_age(birthdate):
    current_date = datetime.now()
    age = current_date - birthdate
    return current_date, current_date.timestamp(), age


def main():
    # Запитуємо користувача про дату народження
    year = int(input("Введіть рік народження (наприклад, 1990): "))
    month = int(input("Введіть місяць народження (від 1 до 12): "))
    day = int(input("Введіть день народження (від 1 до 31): "))

    # Створюємо об'єкт datetime для дати народження
    birth_date = datetime(year, month, day)

    # Визовемо функцію та виведемо результат за допомогою f-стрічок
    current_datetime, current_timestamp, age = calculate_age(birth_date)
    print(f"Поточний час і дата: {current_datetime}")
    print(f"Поточний час у форматі timestamp: {current_timestamp}")
    print(f"Ваш вік: {age}")
    print(f"Ваш вік у форматі timestamp: {age.total_seconds()}")


if __name__ == "__main__":
    main()
