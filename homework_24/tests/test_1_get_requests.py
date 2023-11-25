from homework_24.api import APIRequest
from homework_24.models.object_item import ObjectItem
from homework_24.data.data_handler import DataManager

"""Набір тестів для перевірки роботи API та порівняння даних API з локальними даними."""

data_manager = DataManager("../data/data.json")


def test_get_objects_status_code():
    # Перевіряє код відповіді при запиті всіх об'єктів з API. Очікується, що код
    # відповіді буде 200.
    response = APIRequest.get_objects()
    print("Код статусу відповіді:", response.status_code)
    assert (
        response.status_code == 200
    ), "Очікувався код статусу 200, але отримав {}".format(response.status_code)


def test_get_objects_count():
    # Порівнює кількість об'єктів, отриманих з API, з кількістю об'єктів у локальних
    # даних. Цей тест перевіряє консистентність даних між API та локальним сховищем
    response = APIRequest.get_objects()
    local_data = data_manager.load_data()
    print("Кількість об’єктів у відповіді API:", len(response.json()))
    print("Кількість об'єктів у локальних даних:", len(local_data))
    assert len(response.json()) == len(
        local_data
    ), "Кількість даних API не відповідає кількості локальних даних"


def test_get_specific_object():
    # Виконує запит на отримання конкретного об'єкта за його ідентифікатором з API та
    # порівнює його з локальним об'єктом. Цей тест перевіряє, чи дані конкретного об'єкта у API відповідають даним у
    # локальному сховищі.
    object_id = "6"  # Припустимо, це ідентифікатор існуючого об'єкта
    response = APIRequest.get_single_object(object_id)
    api_object = ObjectItem.from_json(response.json())
    local_object = ObjectItem.from_json(data_manager.get_object_by_id(object_id))
    print("Дані об’єкта API:", api_object.to_json())
    print("Дані локального об'єкта:", local_object.to_json())
    assert (
        api_object.to_json() == local_object.to_json()
    ), "Дані об’єкта API не збігаються з даними локального об’єкта"


def test_objects_have_data():
    # Перевіряє, що кожен об'єкт, отриманий з API, має ключ data. Це забезпечує, що даний
    # ключ є у всіх об'єктах, які повертає API.
    response = APIRequest.get_objects()
    objects = [ObjectItem.from_json(obj) for obj in response.json()]
    for obj in objects:
        print(f"ID об'єкта: {obj.object_id}, Data: {obj.data}")
        assert "data" in obj.__dict__, "Об’єкт не має ключа «data»."
