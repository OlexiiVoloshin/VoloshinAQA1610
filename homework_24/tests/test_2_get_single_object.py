from homework_24.api import APIRequest
from homework_24.data.data_handler import DataManager
from homework_24.models.object_item import ObjectItem

"""Набір тестів для перевірки взаємодії з одиночними об'єктами через API і локальні дані. """

data_manager = DataManager("../data/data.json")


def test_get_single_object_status_code():
    # Набір тестів для перевірки взаємодії з одиночними об'єктами через API і локальні дані.
    response = APIRequest.get_single_object("13")
    print("Код статусу відповіді:", response.status_code)
    assert response.status_code == 200


def test_get_single_object_data():
    # Порівнює дані об'єкта, отримані через API і з локальних даних, для визначення
    # їхньої консистентності. Перевіряє, чи дані об'єкта з ідентифікатором "13" збігаються між API і локальними даними.
    response = APIRequest.get_single_object("13")
    api_object = ObjectItem.from_json(response.json())
    local_object = ObjectItem.from_json(data_manager.get_object_by_id("13"))
    print("Дані об’єкта API:", api_object.to_json())
    print("Дані локального об’єкта:", local_object.to_json())
    assert (
        api_object.to_json() == local_object.to_json()
    ), "Дані об’єкта API не збігаються з даними локального об’єкта"


def test_get_nonexistent_object():
    # Тестує відповідь API на запит неіснуючого об'єкта (з ідентифікатором "9999").
    # Очікується, що код відповіді буде 404, показуючи, що об'єкт не знайдено.
    response = APIRequest.get_single_object("9999")

    # Перевірка типу відповіді та відповідний доступ до status_code
    if isinstance(response, dict):
        # Відповідь у форматі словника
        print("Код статусу відповіді:", response["status_code"])
        assert response["status_code"] == 404
    else:
        # Відповідь у форматі Response
        print("Код статусу відповіді:", response.status_code)
        assert response.status_code == 404


def test_get_object_response_structure():
    # Перевіряє структуру даних об'єкта, отриманого через API. Тестує
    # наявність ключів "id", "name" і "data" у відповіді для об'єкта з ідентифікатором "13".
    response = APIRequest.get_single_object("13")
    api_object = ObjectItem.from_json(response.json())
    print("Дані об’єкта API:", api_object.to_json())
    assert all(
        key in api_object.to_json() for key in ["id", "name", "data"]
    ), "API object data structure is incorrect"
