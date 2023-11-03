import csv
import json


class JSONToCSVAdapter:
    def __init__(self):
        self.__data = []

    def read_json_file(self, filename: str):
        with open(filename, "r") as json_file:
            self.__data = json.load(json_file)
            print("Дані з файлу JSON:")
            print(self.__data)

    def write_csv_file(self, filename: str):
        if not self.__data:
            print("Немає даних для запису в CSV.")
            return

        with open(filename, "w", newline="") as csv_file:
            fieldnames = self.__data[0].keys()
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(self.__data)

    def cleanup(self):
        self.__data = []


# Створення і використання адаптера
adapter = JSONToCSVAdapter()
adapter.read_json_file("example.json")
adapter.write_csv_file("example_converted.csv")

print("Дані успішно конвертовані в CSV у файл 'example_converted.csv'.")
