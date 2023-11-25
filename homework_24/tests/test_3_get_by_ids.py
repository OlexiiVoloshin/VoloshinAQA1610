from homework_24.api import APIRequest
from homework_24.data.data_handler import DataManager
from homework_24.models.object_item import ObjectItem

"""Набір тестів, які перевіряють функціональність отримання об'єктів за їх ідентифікаторами через API та локальний 
менеджер даних (DataManager)"""

# Шлях до файлу з даними
DATA_FILE = "../data/data.json"


def test_get_objects_status_code_api():
    # Перевіряє, що запит до API для отримання всіх об'єктів повертає код
    # статусу 200.
    response = APIRequest.get_objects()
    print("Код статусу відповіді:", response.status_code)
    print("Дані відповіді:", response.json())
    assert response.status_code == 200


def test_get_objects_status_code_data_manager():
    # Перевіряє, що локальні дані можна успішно завантажити за
    # допомогою DataManager.
    data_manager = DataManager(DATA_FILE)
    data = data_manager.load_data()
    assert data is not None
    print("Дані успішно завантажено.")


def test_get_objects_by_ids_status_code_api():
    # Перевіряє, що запит до API для отримання об'єктів за певними
    # ідентифікаторами повертає код статусу 200.
    response = APIRequest.get_objects_by_ids([2, 4, 12])
    print("Код статусу відповіді:", response.status_code)
    print("Дані відповіді :", response.json())
    assert response.status_code == 200


def test_get_objects_by_ids_status_code_data_manager():
    # Перевіряє, що можна відфільтрувати локальні дані за
    # певними ідентифікаторами та отримати очікувану кількість об'єктів.
    data_manager = DataManager(DATA_FILE)
    filtered_data = [
        obj for obj in data_manager.load_data() if obj["id"] in ["2", "4", "12"]
    ]
    assert len(filtered_data) == 3
    print("Відфільтровані дані:", filtered_data)


def test_get_specific_objects_by_ids_api():
    # Перевіряє, що об'єкти, отримані з API за певними ідентифікаторами,
    # відповідають очікуванням.
    response = APIRequest.get_objects_by_ids([2, 4, 12])
    api_objects = [ObjectItem.from_json(obj) for obj in response.json()]
    assert len(api_objects) == 3
    for obj in api_objects:
        print("Об'єкт API:", obj)


def test_get_specific_objects_by_ids_data_manager():
    # Перевіряє, що об'єкти, отримані з локального менеджера даних
    # за певними ідентифікаторами, відповідають очікуванням.
    data_manager = DataManager(DATA_FILE)
    dm_objects = [
        ObjectItem.from_json(obj)
        for obj in data_manager.load_data()
        if obj["id"] in ["2", "4", "12"]
    ]
    assert len(dm_objects) == 3
    for obj in dm_objects:
        print("Об’єкт DataManager:", obj)


def test_get_objects_by_invalid_ids_api():
    # Перевіряє, що запит до API з невалідними ідентифікаторами повертає
    # порожній список об'єктів.
    response = APIRequest.get_objects_by_ids([999, 998])
    api_objects = [ObjectItem.from_json(obj) for obj in response.json()]
    assert len(api_objects) == 0
    print("Відповідь API для недійсного IDs:", api_objects)


def test_get_objects_by_invalid_ids_data_manager():
    # Перевіряє, що спроба відфільтрувати локальні дані за
    # невалідними ідентифікаторами повертає порожній список.
    data_manager = DataManager(DATA_FILE)
    dm_objects = [
        obj for obj in data_manager.load_data() if obj["id"] in ["999", "998"]
    ]
    assert len(dm_objects) == 0
    print("Відповідь DataManager для недійсного IDs:", dm_objects)
