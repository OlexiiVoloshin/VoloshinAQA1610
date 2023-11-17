def find_intersection(arr1, arr2):
    # Використання filter з лямбда-функцією для відбору елементів, що є в обох масивах
    return list(filter(lambda x: x in arr2, arr1))


# Два приклади масивів для демонстрації
array1 = [1, 2, 3, 4, 5]
array2 = [4, 5, 6, 7, 8]

# Виклик функції та виведення результату
intersection = find_intersection(array1, array2)
print("Перетин масивів:", intersection)
