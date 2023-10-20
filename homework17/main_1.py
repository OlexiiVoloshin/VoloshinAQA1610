from datetime import datetime, timedelta


def modify_date(input_date, days, add=True):
    """
    Додати або відняти певну кількість днів від заданої дати та часу.

    :param input_date: Початкова дата та час (datetime)
    :param days: Кількість днів для додавання або віднімання (int)
    :param add: Якщо True, додаємо дні; якщо False, віднімаємо дні (bool)
    :return: Змінена дата та час (datetime)
    """
    if add:
        modified_date = input_date + timedelta(days=days)
    else:
        modified_date = input_date - timedelta(days=days)
    return modified_date


def main():
    date_str = input("Введіть дату та час у форматі 'рік-місяць-день година:хвилини': ")
    input_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")

    days = int(input("Введіть кількість днів для додавання або віднімання: "))
    add = (
        input("Введіть 'True' для додавання днів, 'False' для віднімання: ").lower()
        == "true"
    )

    new_date = modify_date(input_date, days, add)
    print(f"Результат: {new_date}")


if __name__ == "__main__":
    main()
