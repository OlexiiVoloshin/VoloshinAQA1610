import csv


def add_row_to_csv(filename, data):
    try:
        with open(filename, "a", newline="") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=data.keys())
            if csv_file.tell() == 0:
                writer.writeheader()
            writer.writerow(data)
    except Exception as e:
        print(f"Помилка при додаванні рядка до CSV: {e}")


if __name__ == "__main__":
    # Приклад використання
    row_data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": "25",
        "gender": "Male",
        "salary": "5000",
    }
    add_row_to_csv("example.csv", row_data)
