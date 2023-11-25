import json


class DataManager:
    def __init__(self, data_file):
        self.data_file = data_file

    def load_data(
        self,
    ):  # Завантажує дані з файлу JSON. Використовується для читання даних з файлу.
        with open(self.data_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def save_data(
        self, data
    ):  # Зберігає змінені дані у файлі JSON. Використовується для запису даних у
        # файл.
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def get_object_by_id(
        self, object_id
    ):  # Повертає об'єкт за вказаним ідентифікатором. Якщо об'єкт не знайдено,
        # повертає None.
        data = self.load_data()
        return next((obj for obj in data if obj.get("id") == object_id), None)

    def add_object(
        self, object_data
    ):  # Додає новий об'єкт до даних. Генерує новий ідентифікатор для об'єкта та
        # зберігає його у файлі.
        data = self.load_data()
        new_id = str(max([int(obj.get("id", 0)) for obj in data]) + 1)
        new_object = {
            "id": new_id,
            "name": object_data.get("name", ""),
            "data": object_data.get("data", {}),
        }

        data.append(new_object)
        self.save_data(data)

    def update_object(
        self, object_id, new_data
    ):  # Оновлює існуючий об'єкт з новими даними. Якщо об'єкт знайдено,
        # він оновлюється та зберігається у файлі.
        data = self.load_data()
        for obj in data:
            if obj["id"] == object_id:
                for key in new_data:
                    if key in obj:
                        obj[key] = new_data[key]
                break
        self.save_data(data)

    def delete_object(
        self, object_id
    ):  # Видаляє об'єкт за вказаним ідентифікатором. Об'єкт видаляється з даних і
        # збережені зміни у файлі.
        data = self.load_data()
        data = [obj for obj in data if obj["id"] != object_id]
        self.save_data(data)
