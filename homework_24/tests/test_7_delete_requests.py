from homework_24.data.data_handler import DataManager
from homework_24.models.object_item import ObjectItem


""" Набір тестів для перевірки функціональності видалення об'єктів, використовуючи клас DataManager."""


DATA_FILE = "../data/data.json"


def test_delete_object_status_code():
    # Перевіряє, чи успішно видаляється об'єкт з заданим ідентифікатором ("6") за допомогою ObjectItem.
    data_manager = DataManager(DATA_FILE)
    data_manager.delete_object("6")
    deleted_object_data = data_manager.get_object_by_id("6")
    deleted_object = (
        ObjectItem.from_json(deleted_object_data) if deleted_object_data else None
    )
    assert deleted_object is None
    print(
        "Об'єкт з ідентифікатором 6 успішно видалено. Відповідь: {}".format(
            deleted_object
        )
    )


def test_delete_object_response_message():
    # Підтверджує, що об'єкт з заданим ідентифікатором ("6") видалений, використовуючи ObjectItem.
    data_manager = DataManager(DATA_FILE)
    data_manager.delete_object("6")
    deleted_object_data = data_manager.get_object_by_id("6")
    deleted_object = (
        ObjectItem.from_json(deleted_object_data) if deleted_object_data else None
    )
    assert deleted_object is None
    print("Підтверджено: об’єкт з ID 6 видалено. Відповідь: {}".format(deleted_object))


def test_delete_nonexistent_object():
    # Перевіряє спробу видалення неіснуючого об'єкта (з ідентифікатором "9999").
    data_manager = DataManager(DATA_FILE)
    data_manager.delete_object("9999")
    nonexistent_object_data = data_manager.get_object_by_id("9999")
    nonexistent_object = (
        ObjectItem.from_json(nonexistent_object_data)
        if nonexistent_object_data
        else None
    )
    assert nonexistent_object is None
    print(
        "Спробу видалення неіснуючого об’єкта виконано. Відповідь: {}".format(
            nonexistent_object
        )
    )


def test_delete_object_and_verify():
    # Виконує додавання, видалення та перевірку об'єкта за допомогою ObjectItem.
    data_manager = DataManager(DATA_FILE)
    new_object_data = {"name": "Test Object", "data": {}}
    data_manager.add_object(new_object_data)
    new_object_id = str(
        int(max([obj.get("id", 0) for obj in data_manager.load_data()]))
    )

    data_manager.delete_object(new_object_id)
    deleted_object_data = data_manager.get_object_by_id(new_object_id)
    deleted_object = (
        ObjectItem.from_json(deleted_object_data) if deleted_object_data else None
    )
    assert deleted_object is None
    print(
        f"Перевірка після видалення: Об'єкт з ID {new_object_id} видаляється. Відповідь: {deleted_object}"
    )
