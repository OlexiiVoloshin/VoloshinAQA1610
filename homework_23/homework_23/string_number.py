def main():
    """
    Головна функція програми.
    """
    while True:
        # Запит вводу від користувача
        user_input = input("Введіть рядок для перевірки, або 'exit' для виходу: ")

        # Перевірка на команду виходу
        if user_input.lower() == 'exit':
            print("Програма завершена.")
            break

        # Використання лямбда-функції без присвоєння
        result = (lambda s: s.replace('.', '', 1).isdigit() and s.count('.') < 2)(user_input)

        # Виведення результату
        print(f"Рядок '{user_input}' є числом: {result}")


if __name__ == "__main__":
    main()
