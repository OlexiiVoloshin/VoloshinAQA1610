import json


class ObjectItem:
    def __init__(self, object_id, name, data=None, created_at=None, updated_at=None):
        self.object_id = object_id
        self.name = name
        self.data = data if data is not None else {}
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_json(
        cls, json_data
    ):  # Це класовий метод, який приймає дані у форматі JSON і конвертує їх у екземпляр
        # класу ObjectItem. Метод повертає об'єкт ObjectItem, ініціалізований даними з JSON.
        object_id = json_data.get("id")
        name = json_data.get("name", "")
        data = json_data.get("data", {})
        created_at = json_data.get("createdAt")
        updated_at = json_data.get("updatedAt")

        return cls(
            object_id=object_id,
            name=name,
            data=data,
            created_at=created_at,
            updated_at=updated_at,
        )

    def to_json(
        self,
    ):  # Метод конвертує об'єкт ObjectItem назад у формат JSON. Це зручно для передачі даних між
        # різними частинами програми або для збереження даних у файлі.
        return {
            "id": self.object_id,
            "name": self.name,
            "data": self.data,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=4)
