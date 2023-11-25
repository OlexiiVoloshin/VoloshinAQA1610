from homework_24.data.data_handler import DataManager
from homework_24.models.object_item import ObjectItem

"""Набір тестів для перевірки функціональності додавання нових об'єктів у локальне сховище даних через DataManager"""

DATA_FILE = "../data/data.json"


def get_next_id():
    # Визначає наступний унікальний ідентифікатор (ID) для нового об'єкта, заснований на існуючих даних.
    data_manager = DataManager(DATA_FILE)
    data = data_manager.load_data()
    return str(max([int(obj.get("id", 0)) for obj in data]) + 1) if data else "1"


def test_post_add_object_status_code():
    # Перевіряє, чи успішно додається новий об'єкт до локальних даних.
    # Демонструє, що об'єкт було додано без помилок
    data_manager = DataManager(DATA_FILE)
    expected_id = get_next_id()  # Отримуємо наступний ID перед додаванням об'єкта
    new_object_data = {
        "name": "XIAOMI 13T Pro",
        "data": {"color": "Cloudy White", "capacity GB": 512},
    }
    data_manager.add_object(new_object_data)
    print("Об'єкт успішно додано.")
    added_object = data_manager.get_object_by_id(expected_id)
    print(f"Тіло відповіді після додавання об'єкта: {added_object}")

    # Перевіряємо, що доданий об'єкт відповідає новому об'єкту
    assert added_object and added_object["id"] == expected_id
    assert added_object["name"] == new_object_data["name"]
    assert added_object["data"] == new_object_data["data"]


def test_post_add_object_response():
    # Перевіряє, чи ідентифікатор доданого об'єкта відповідає очікуваному новому
    # ідентифікатору. Виводить ідентифікатор доданого об'єкта.
    data_manager = DataManager(DATA_FILE)
    new_object_data = {
        "name": "XIAOMI 13T Pro",
        "data": {"color": "Cloudy White", "capacity GB": 512},
    }
    expected_id = get_next_id()
    data_manager.add_object(new_object_data)
    added_object = data_manager.get_object_by_id(expected_id)
    assert added_object and added_object["id"] == expected_id
    print(f"Додано ідентифікатор об'єкта: {added_object['id']}")
    print(f"Тіло відповіді після додавання об'єкта: {added_object}")


def test_post_response_structure():
    # Перевіряє структуру даних доданого об'єкта, зокрема наявність ключових
    # атрибутів (object_id, name, data). Виводить дані відповіді для огляду.
    data_manager = DataManager(DATA_FILE)
    new_object_data = {
        "name": "XIAOMI 13T Pro",
        "data": {"color": "Cloudy White", "capacity GB": 512},
    }
    data_manager.add_object(new_object_data)
    added_object = data_manager.get_object_by_id(get_next_id())
    if added_object:
        response_object = ObjectItem.from_json(added_object)
        print(f"Об'єкт відповіді: {response_object.__dict__}")
        assert hasattr(response_object, "object_id")
        assert hasattr(response_object, "name")
        assert hasattr(response_object, "data")


def test_post_with_partial_data():
    # Перевіряє можливість додавання об'єкта з частковими даними (тільки з назвою,
    # без додаткових даних). Виводить інформацію про доданий об'єкт з частковими даними.
    data_manager = DataManager(DATA_FILE)
    partial_object_data = {"name": "XIAOMI 14T Pro"}
    expected_id = get_next_id()
    data_manager.add_object(partial_object_data)
    added_object = data_manager.get_object_by_id(expected_id)
    assert added_object and added_object["id"] == expected_id
    print(f"Додано об’єкт із частковими даними: {added_object}")
    print(f"Тіло відповіді після додавання об'єкта: {added_object}")
