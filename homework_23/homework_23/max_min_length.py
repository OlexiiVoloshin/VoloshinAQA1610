def find_lists_with_extreme_lengths(input_lists):
    # Функція для знаходження довжини списку
    def list_length(x):
        return len(x)

    # Знаходимо список з максимальною довжиною
    max_length_list = max(input_lists, key=list_length)

    # Знаходимо список з мінімальною довжиною
    min_length_list = min(input_lists, key=list_length)

    return max_length_list, min_length_list


# Тестуємо функцію
lists_to_test = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10], [11, 12, 13]]
max_list, min_list = find_lists_with_extreme_lengths(lists_to_test)

print("Список з максимальною довжиною:", max_list)
print("Список з мінімальною довжиною:", min_list)
