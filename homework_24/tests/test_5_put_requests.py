from homework_24.data.data_handler import DataManager
from homework_24.models.object_item import ObjectItem

"""Набір тестів для перевірки функціональності оновлення об'єктів у локальному сховищі даних через DataManager."""

DATA_FILE = "../data/data.json"


def test_put_update_object_status_code():
    # Перевіряє, чи можна успішно оновити існуючий об'єкт за допомогою
    # вказаного ідентифікатора та даних. Очікується, що ціна та колір об'єкта будуть оновлені.
    data_manager = DataManager(DATA_FILE)
    update_data = {
        "name": "Apple AirPods",
        "data": {"color": "white", "generation": "3rd", "price": 135},
    }
    data_manager.update_object("6", update_data)
    updated_object = data_manager.get_object_by_id("6")
    print(f"Оновлений об'єкт: {updated_object}")
    assert updated_object["id"] == "6"
    assert updated_object["data"]["price"] == 135
    assert updated_object["data"]["color"] == "white"


def test_put_update_object_response():
    # Подібно до попереднього тесту, але також перевіряє, чи відповідь відповідає
    # очікуваній за допомогою класу ObjectItem.
    data_manager = DataManager(DATA_FILE)
    update_data = {
        "name": "Apple AirPods",
        "data": {"color": "white", "generation": "3rd", "price": 135},
    }
    data_manager.update_object("6", update_data)
    updated_object = data_manager.get_object_by_id("6")
    object_item = ObjectItem.from_json(updated_object)
    print(f"Оновлений об'єкт: {object_item.__dict__}")
    assert object_item.object_id == "6"
    assert object_item.data["price"] == 135
    assert object_item.data["color"] == "white"


def test_put_nonexistent_object():
    # Перевіряє відсутність змін після спроби оновити неіснуючий об'єкт. Очікується,
    # що не буде жодних оновлень, оскільки об'єкт не знайдений.
    data_manager = DataManager(DATA_FILE)
    update_data = {"name": "Nonexistent Object", "data": {}}
    response = data_manager.update_object("9999", update_data)
    assert response is None
    print("Немає оновлень для неіснуючого об’єкта.")


def test_put_object_invalid_data():
    # Перевіряє, що оновлення не відбувається при спробі внести неправильні дані.
    # Підтверджує відсутність змін у об'єкті після спроби оновлення.
    data_manager = DataManager(DATA_FILE)
    invalid_update_data = {"invalidField": "Invalid"}
    response = data_manager.update_object("6", invalid_update_data)
    assert response is None
    print("Оновлення не виконано через недійсні дані.")


def test_put_partial_update_object():
    # Перевіряє можливість часткового оновлення об'єкта, наприклад, оновлення лише
    # назви. Виводить оновлений об'єкт для перевірки.
    data_manager = DataManager(DATA_FILE)
    partial_update_data = {"name": "Apple AirPods Updated"}
    data_manager.update_object("6", partial_update_data)
    updated_object = data_manager.get_object_by_id("6")
    assert updated_object["name"] == "Apple AirPods Updated"
    print(f"Частково оновлений об'єкт: {updated_object}")


def test_put_update_with_wrong_keys():
    # Перевіряє, що неправильні ключі не впливають на оновлення об'єкта.
    # Очікується, що об'єкт не містить нових неправильних полів після оновлення.
    data_manager = DataManager(DATA_FILE)
    wrong_update_data = {"invalidField": "Invalid", "anotherWrongField": 123}
    data_manager.update_object("6", wrong_update_data)
    updated_object = data_manager.get_object_by_id("6")
    assert (
        "invalidField" not in updated_object
        and "anotherWrongField" not in updated_object
    )
    print(f"Об’єкт після спроби оновлення неправильних полів: {updated_object}")
