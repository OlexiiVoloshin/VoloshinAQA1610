import os
import pytest
from add_row_to_csv import add_row_to_csv
from delete_row_from_csv import delete_row_from_csv


# Перевірка додавання рядка до CSV
def test_add_row_to_csv():
    row_data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": "25",
        "gender": "Male",
        "salary": "5000",
    }
    add_row_to_csv("example_test.csv", row_data)
    assert os.path.exists("example_test.csv")


# Перевірка видалення рядка з CSV
def test_delete_row_from_csv():
    # Спочатку додаємо рядок для подальшого видалення
    row_data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": "25",
        "gender": "Male",
        "salary": "5000",
    }
    add_row_to_csv("example_test.csv", row_data)

    delete_row_from_csv("example_test.csv", 0)  # Видаляємо перший рядок
    assert os.path.exists("example_test.csv")


if __name__ == "__main__":
    pytest.main()
