import random


def main():
    # Створення списку з 100 елементів
    my_list = [random.randint(1, 10) for _ in range(100)]

    # Підрахунок кількості кожного елемента
    count_dict = {i: my_list.count(i) for i in range(1, 11)}

    # Виведення результатів
    for key, value in count_dict.items():
        print(f"Число {key} зустрічається {value} разів.")


if __name__ == "__main__":
    main()
