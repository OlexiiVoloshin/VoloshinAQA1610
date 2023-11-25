from homework_24.data.data_handler import DataManager
from homework_24.models.object_item import ObjectItem

DATA_FILE = "../data/data.json"


def test_patch_update_object_status_code():
    # Перевірка часткового оновлення об'єкта (тільки назва).
    data_manager = DataManager(DATA_FILE)
    patch_data = {"name": "Apple MacBook Pro 18 (Updated Name)"}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(f"Дані відповіді після часткового оновлення: {updated_object.to_json()}")


def test_patch_nonexistent_object():
    # Перевірка відсутності змін для неіснуючого об'єкта.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"name": "Samsung"}
    data_manager.update_object("9999", patch_data)
    updated_object = data_manager.get_object_by_id("9999")
    print(f"Відповідь на неіснуючий об’єкт: {updated_object}")


def test_patch_object_invalid_field():
    # Перевірка, що недійсні поля не додаються.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"invalidField": "Invalid"}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(
        f"Дані відповіді після спроби недійсного оновлення: {updated_object.to_json()}"
    )


def test_patch_multiple_fields():
    # Перевірка оновлення декількох полів одночасно.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"name": "New MacBook Pro", "data": {"price": 1999.99}}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(f"Дані відповіді після оновлення кількох полів: {updated_object.to_json()}")


def test_patch_with_empty_data():
    # Перевірка, що порожній патч не впливає на об'єкт.
    data_manager = DataManager(DATA_FILE)
    patch_data = {}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(f"Дані відповіді після порожнього патча: {updated_object.to_json()}")


def test_patch_with_null_data():
    # Перевірка скидання поля data до порожнього словника.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"data": None}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(
        f"Дані відповіді після виправлення нульових даних: {updated_object.to_json()}"
    )


def test_patch_update_with_empty_name():
    # Перевірка зміни назви на порожній рядок.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"name": ""}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(
        f"Дані відповіді після оновлення імені до порожнього рядка: {updated_object.to_json()}"
    )


def test_patch_update_with_null_name():
    # Перевірка зміни назви на None.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"name": None}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(f"Дані відповіді після оновлення імені на 'None': {updated_object.to_json()}")


def test_patch_update_with_additional_field():
    # Перевірка відсутності додавання нових полів.
    data_manager = DataManager(DATA_FILE)
    patch_data = {"newField": "New Value"}
    data_manager.update_object("7", patch_data)
    updated_object = ObjectItem.from_json(data_manager.get_object_by_id("7"))
    print(
        f"Дані відповіді після спроби оновлення додаткового поля: {updated_object.to_json()}"
    )
