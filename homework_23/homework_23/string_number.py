def is_number(string):
    """
    Функція для перевірки, чи є рядок числом.
    Перевіряє, чи складається рядок тільки з цифр та містить не більше однієї крапки.
    """
    try:
        float(string)
        return True
    except ValueError:
        return False


def main():
    """
    Головна функція програми.
    """
    while True:
        # Запит вводу від користувача
        user_input = input("Введіть рядок для перевірки, або 'exit' для виходу: ")

        # Перевірка на команду виходу
        if user_input.lower() == "exit":
            print("Програма завершена.")
            break

        # Виведення результату
        result = is_number(user_input)
        print(f"Рядок '{user_input}' є числом: {result}")


if __name__ == "__main__":
    main()
