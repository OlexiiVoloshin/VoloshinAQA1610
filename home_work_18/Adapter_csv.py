import csv
import json


class CSVToJSONAdapter:
    def __init__(self):
        self.__data = []

    def read_csv_file(self, filename: str):
        with open(filename, "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                self.__data.append(row)
            print("Дані з файлу CSV:")
            print(self.__data)

    def write_json_file(self, filename: str):
        if not self.__data:
            print("Немає даних для запису в JSON.")
            return

        with open(filename, "w") as json_file:
            json.dump(self.__data, json_file, indent=4)

    def cleanup(self):
        self.__data = []


# Створення і використання адаптера
adapter = CSVToJSONAdapter()
adapter.read_csv_file("example.csv")
adapter.write_json_file("example_converted.json")

print("Дані успішно конвертовані в JSON у файл 'example_reconverted.json'.")
