import json
import unittest
from homework_26.api_db_adapter import ApiDbAdapter


class TestApiDbAdapter(unittest.TestCase):
    def setUp(self):
        db_config = {
            "host": "localhost",
            "port": 3306,
            "user": "root",
            "password": "tteerrii13",
            "database": "restful_api",
        }
        self.adapter = ApiDbAdapter(db_config)

    # Тести для взаємодії з API
    def test_fetch_from_api_and_insert_to_db(self):
        api_data = self.adapter.fetch_from_api_and_insert_to_db("objects")
        self.assertIsNotNone(api_data)
        self.assertTrue(len(api_data) > 0)

        # Додаткова перевірка: читаємо з бази даних
        query = "SELECT * FROM api_data"
        db_data = self.adapter.fetch_from_db(query)
        self.assertTrue(len(db_data) > 0)

    def test_get_all_objects_from_api(self):
        all_objects = self.adapter.get_all_objects()
        print("Всі об'єкти:", json.dumps(all_objects, indent=4))
        self.assertIsNotNone(all_objects)

    def test_get_specific_objects_by_ids_from_api(self):
        specific_objects = self.adapter.get_objects_by_ids([3, 5, 10])
        print("Об'єкти за ID:", json.dumps(specific_objects, indent=4))
        self.assertIsNotNone(specific_objects)
        self.assertEqual(len(specific_objects), 3)

    def test_get_single_object_from_api(self):
        single_object = self.adapter.get_single_object(7)
        print("Один об'єкт:", json.dumps(single_object, indent=4))
        self.assertIsNotNone(single_object)
        self.assertEqual(single_object["id"], "7")

    def test_add_object_via_api(self):
        new_object_data = {
            "name": "Apple MacBook Pro 16",
            "data": {
                "year": 2022,
                "price": 2849.99,
                "CPU model": "Intel Core i9",
                "Hard disk size": "1 TB",
            },
        }
        response = self.adapter.add_object(new_object_data)
        print("Відповідь на POST-запит:", json.dumps(response, indent=4))
        self.assertIsNotNone(response)
        self.assertEqual(response["name"], new_object_data["name"])

    # Тести для взаємодії з базою даних
    def test_update_object_in_db(self):
        object_id = 7
        new_name = "Updated Name"
        new_data = {"year": 2020, "price": 1999.99}

        # Оновлюємо об'єкт
        self.adapter.update_object_in_db(object_id, new_name, new_data)

        # Перевіряємо, чи оновлення відбулося
        query = "SELECT name, data FROM api_data WHERE id = %s"
        result = self.adapter.fetch_from_db(query, (object_id,))
        updated_object = {"name": result[0][0], "data": json.loads(result[0][1])}
        print("Оновлений об'єкт:", json.dumps(updated_object, indent=4))
        self.assertEqual(result[0][0], new_name)  # Перевіряємо ім'я
        self.assertEqual(json.loads(result[0][1]), new_data)  # Перевіряємо дані

    def test_update_full_object_in_db(self):
        object_id = 7
        new_name = "Xiomi"
        new_data = {"year": 2021, "price": 2099.99}

        # Оновлюємо об'єкт
        self.adapter.update_full_object_in_db(object_id, new_name, new_data)

        # Перевіряємо, чи оновлення відбулося
        query = "SELECT name, data FROM api_data WHERE id = %s"
        result = self.adapter.fetch_from_db(query, (object_id,))
        fully_updated_object = {"name": result[0][0], "data": json.loads(result[0][1])}
        print("Повністю оновлений об'єкт:", json.dumps(fully_updated_object, indent=4))
        self.assertEqual(result[0][0], new_name)  # Перевіряємо ім'я
        self.assertEqual(json.loads(result[0][1]), new_data)  # Перевіряємо дані

    # Тести для інтеграції API і бази даних

    def test_full_cycle_api_db_integration(self):
        # Створюємо новий об'єкт через API
        new_object_data = {"name": "New Object", "data": {"attribute": "value"}}
        post_response = self.adapter.send_to_api("objects", new_object_data)
        self.assertIsNotNone(post_response)
        print("Створено об'єкт через API:")
        print(
            json.dumps(
                post_response, ensure_ascii=False, indent=4, separators=(",", ": ")
            )
        )

        # Перевіряємо створення об'єкта через API
        get_response = self.adapter.fetch_from_api(f"objects/{post_response['id']}")
        self.assertIsNotNone(get_response)
        print("Запит до API для отримання об'єкта:")
        print(
            json.dumps(
                get_response, ensure_ascii=False, indent=4, separators=(",", ": ")
            )
        )

        # Записуємо об'єкт в базу даних
        self.adapter.send_to_db(
            "INSERT INTO api_data (api_id, name, data) VALUES (%s, %s, %s)",
            (
                post_response["id"],
                post_response["name"],
                json.dumps(post_response["data"]),
            ),
        )
        print("Запис об'єкта в базу даних.")

        # Перевіряємо запис в базі даних
        db_response = self.adapter.fetch_from_db(
            "SELECT name, data FROM api_data WHERE api_id = %s", (post_response["id"],)
        )
        print("Запит до бази даних для перевірки запису:")
        print(f"Ім'я: {db_response[0][0]}")
        print("Дані:")
        print(json.loads(db_response[0][1]))
        self.assertEqual(db_response[0][0], new_object_data["name"])
        self.assertEqual(json.loads(db_response[0][1]), new_object_data["data"])

    def test_api_to_sql_post_get(self):
        # Створюємо новий об'єкт через API
        new_object_data = {"name": "New Object", "data": {"attribute": "value"}}
        post_response = self.adapter.send_to_api("objects", new_object_data)
        self.assertIsNotNone(post_response)

        # Отримуємо об'єкт через API
        get_response = self.adapter.fetch_from_api(f"objects/{post_response['id']}")
        self.assertIsNotNone(get_response)

        # Записуємо об'єкт в базу даних
        self.adapter.send_to_db(
            "INSERT INTO api_data (api_id, name, data) VALUES (%s, %s, %s)",
            (
                post_response["id"],
                post_response["name"],
                json.dumps(post_response["data"]),
            ),
        )

        # Перевіряємо запис в базі даних
        db_response = self.adapter.fetch_from_db(
            "SELECT name, data FROM api_data WHERE api_id = %s", (post_response["id"],)
        )
        self.assertEqual(db_response[0][0], new_object_data["name"])
        self.assertEqual(json.loads(db_response[0][1]), new_object_data["data"])
        print("POST Response:", json.dumps(post_response, indent=4))
        print("GET Response:", json.dumps(get_response, indent=4))
        print("DB Response:", json.dumps(db_response, indent=4))

    def test_sql_to_api_insert_get(self):
        # Створюємо новий об'єкт в базі даних
        new_object_data = {"name": "New Object", "data": {"attribute": "value"}}
        self.adapter.send_to_db(
            "INSERT INTO api_data (name, data) VALUES (%s, %s)",
            (new_object_data["name"], json.dumps(new_object_data["data"])),
        )

        # Отримуємо об'єкт з бази даних
        query = "SELECT id, name, data FROM api_data WHERE name = %s"
        db_response = self.adapter.fetch_from_db(query, (new_object_data["name"],))
        self.assertIsNotNone(db_response)
        object_id = db_response[0][0]

        # Отправляємо запит до API для отримання об'єкта
        get_response = self.adapter.fetch_from_api(f"objects/{object_id}")
        self.assertIsNotNone(get_response)
        print("DB Response:", json.dumps(db_response, indent=4))
        print("GET Response:", json.dumps(get_response, indent=4))

    def test_sql_to_api_update_get(self):
        # Створюємо новий об'єкт в базі даних
        new_object_data = {"name": "New Object", "data": {"attribute": "value"}}
        self.adapter.send_to_db(
            "INSERT INTO api_data (name, data) VALUES (%s, %s)",
            (new_object_data["name"], json.dumps(new_object_data["data"])),
        )

        # Отримуємо об'єкт з бази даних
        query = "SELECT id, name, data FROM api_data WHERE name = %s"
        db_response = self.adapter.fetch_from_db(query, (new_object_data["name"],))
        self.assertIsNotNone(db_response)
        object_id = db_response[0][0]

        # Оновлюємо об'єкт в базі даних
        updated_name = "Updated Name"
        updated_data = {"year": 2022, "price": 2999.99}
        self.adapter.update_object_in_db(object_id, updated_name, updated_data)

        # Отправляємо запит до API для отримання оновленого об'єкта
        get_response = self.adapter.fetch_from_api(f"objects/{object_id}")
        self.assertIsNotNone(get_response)
        print("DB Response:", json.dumps(db_response, indent=4))
        print("GET Response:", json.dumps(get_response, indent=4))

    def test_post_get_insert_select(self):
        # Створення об'єкта через API
        new_object_data = {"name": "Test Object", "data": {"attribute": "value"}}
        post_response = self.adapter.send_to_api("objects", new_object_data)
        self.assertIsNotNone(post_response)

        # Перевірка через GET запит
        get_response = self.adapter.fetch_from_api(f"objects/{post_response['id']}")
        self.assertIsNotNone(get_response)

        # Вставка в SQL і перевірка через SELECT
        self.adapter.send_to_db(
            "INSERT INTO api_data (api_id, name, data) VALUES (%s, %s, %s)",
            (
                post_response["id"],
                post_response["name"],
                json.dumps(post_response["data"]),
            ),
        )
        db_response = self.adapter.fetch_from_db(
            "SELECT name, data FROM api_data WHERE api_id = %s", (post_response["id"],)
        )
        self.assertEqual(db_response[0][0], new_object_data["name"])
        print("POST Response:", json.dumps(post_response, indent=4))
        print("GET Response:", json.dumps(get_response, indent=4))
        print("DB Response:", json.dumps(db_response, indent=4))

    def test_put_get_update_select(self):
        # Створення нового об'єкта через API
        new_object_data = {
            "name": "New Object for PUT",
            "data": {"attribute": "initial value"},
        }
        post_response = self.adapter.send_to_api("objects", new_object_data)
        self.assertIsNotNone(post_response)
        object_id = post_response["id"]

        # Оновлення створеного об'єкта через API
        updated_data = {"name": "Updated Object", "data": {"attribute": "new value"}}
        self.adapter.put_and_update(object_id, "objects", updated_data)

        # Перевірка через GET запит
        get_response = self.adapter.fetch_from_api(f"objects/{object_id}")
        print("GET Response:", json.dumps(get_response, indent=4))
        self.assertEqual(get_response["name"], updated_data["name"])

    def test_update_select_put_get(self):
        # Створення нового об'єкта через API
        new_object_data = {
            "name": "New Object for Update",
            "data": {"attribute": "initial value"},
        }
        post_response = self.adapter.send_to_api("objects", new_object_data)
        self.assertIsNotNone(post_response)
        object_id = post_response["id"]

        # Оновлення запису в базі даних
        updated_data = {
            "name": "Updated Object DB",
            "data": {"attribute": "new value DB"},
        }
        self.adapter.update_object_in_db(
            object_id, updated_data["name"], updated_data["data"]
        )

        # Перевірка через SELECT запит до бази даних
        select_query = "SELECT name, data FROM api_data WHERE api_id = %s"
        db_response = self.adapter.fetch_from_db(select_query, (object_id,))
        print("DB SELECT Response:", json.dumps(db_response, indent=4))
        self.assertEqual(db_response[0][0], updated_data["name"])
        self.assertEqual(json.loads(db_response[0][1]), updated_data["data"])

        # Перевірка через GET запит
        get_response = self.adapter.fetch_from_api(f"objects/{object_id}")
        print("GET Response:", json.dumps(get_response, indent=4))
        self.assertEqual(get_response["name"], updated_data["name"])
        self.assertEqual(get_response["data"], updated_data["data"])

        # Перевірка, чи db_response містить дані
        self.assertTrue(
            len(db_response) > 0, "No data found in the database for the given api_id"
        )
        self.assertEqual(db_response[0][0], updated_data["name"])
        self.assertEqual(json.loads(db_response[0][1]), updated_data["data"])

    def tearDown(self):
        self.adapter.close()


if __name__ == "__main__":
    unittest.main()
