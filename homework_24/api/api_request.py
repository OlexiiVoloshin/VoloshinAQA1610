import datetime
import json
import os
import requests


class APIRequest:
    BASE_URL = "https://api.restful-api.dev/"
    DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "data.json")

    @staticmethod
    def get_objects():  # Запит на отримання всіх об'єктів з API.
        response = requests.get(APIRequest.BASE_URL + "objects")
        return response

    @staticmethod
    def get_objects_by_ids(ids):  # Запит на отримання об'єктів за їх ідентифікаторами.
        params = {"id": ids}
        response = requests.get(APIRequest.BASE_URL + "objects", params=params)
        return response

    @staticmethod
    def get_single_object(
        object_id,
    ):  # Запит на отримання одного об'єкта за ідентифікатором. Якщо об'єкт не
        # знайдено, генерується помилка HTTP.
        try:
            response = requests.get(APIRequest.BASE_URL + f"objects/{object_id}")
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as e:
            return {"status_code": e.response.status_code, "message": str(e)}

    @staticmethod
    def load_data():  # Завантажує дані з локального файлу JSON.
        with open(APIRequest.DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def save_data(data):  # Зберігає дані у локальний файл JSON
        with open(APIRequest.DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    @staticmethod
    def post_add_object(
        data,
    ):  # Створює новий об'єкт з даними, отриманими в параметрах, та зберігає його у
        # локальному файлі.
        objects = APIRequest.load_data()
        new_id = str(max([int(obj["id"]) for obj in objects]) + 1) if objects else "1"
        new_object = {
            "id": new_id,
            "name": data.get("name", ""),
            "data": data.get("data", {}),
        }
        objects.append(new_object)
        APIRequest.save_data(objects)
        return {"status_code": 200, "data": new_object}

    @staticmethod
    def put_update_object(
        object_id, data
    ):  # Оновлює об'єкт за його ідентифікатором з новими даними.
        objects = APIRequest.load_data()
        updated_obj = None
        for obj in objects:
            if obj["id"] == object_id:
                obj.update(data)
                obj["updatedAt"] = datetime.datetime.now().isoformat()
                updated_obj = obj
                break
        if updated_obj:
            APIRequest.save_data(objects)
            return {"status_code": 200, "data": updated_obj}
        else:
            return {"status_code": 404, "message": "Object not found"}

    @staticmethod
    def patch_update_object(
        object_id, data
    ):  # Оновлює частину даних об'єкта за його ідентифікатором.
        objects = APIRequest.load_data()
        updated_obj = None
        for obj in objects:
            if obj["id"] == object_id:
                for key, value in data.items():
                    if key in obj:
                        obj[key] = value
                obj["updatedAt"] = datetime.datetime.now().isoformat()
                updated_obj = obj
                break
        if updated_obj:
            APIRequest.save_data(objects)
            return {"status_code": 200, "data": updated_obj}
        else:
            return {"status_code": 404, "message": "Object not found"}

    @staticmethod
    def delete_object(object_id):  # Видаляє об'єкт за його ідентифікатором.
        objects = APIRequest.load_data()
        objects = [obj for obj in objects if obj["id"] != object_id]
        APIRequest.save_data(objects)
        return {
            "status_code": 200,
            "message": f"Object with id {object_id} deleted successfully",
        }

    @staticmethod
    def get_single_object_test_version(
        object_id,
    ):  # Тестова версія методу для отримання одного об'єкта,
        # використовується для перевірки видалення об'єктів.
        objects = APIRequest.load_data()
        for obj in objects:
            if obj["id"] == object_id:
                return {"status_code": 200, "data": obj}
        return {"status_code": 404, "message": f"Object with id {object_id} not found"}
