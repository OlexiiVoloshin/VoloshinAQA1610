import csv


def delete_row_from_csv(filename, row_index):
    try:
        with open(filename, "r", newline="") as csv_file:
            lines = list(csv.DictReader(csv_file))
            if 0 <= row_index < len(lines):
                del lines[row_index]
            else:
                print("Недійсний індекс рядка для видалення.")
                return

        with open(filename, "w", newline="") as csv_file:
            fieldnames = lines[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(lines)
    except Exception as e:
        print(f"Помилка при видаленні рядка з CSV: {e}")


if __name__ == "__main__":
    # Приклад використання
    delete_row_from_csv("example.csv", 2)  # Видалити третій рядок (індекс 2)
