import json
import requests
import pymysql


class ApiDbAdapter:
    def __init__(self, db_config):
        self.api_url = "https://api.restful-api.dev/"
        self.db = pymysql.connect(**db_config)

    def send_to_api(self, endpoint, data, method="post"):
        url = self.api_url + endpoint
        if method.lower() == "post":
            response = requests.post(url, json=data)
        elif method.lower() == "put":
            response = requests.put(url, json=data)
        elif method.lower() == "patch":
            response = requests.patch(url, json=data)
        else:
            raise ValueError(f"Unsupported method: {method}")
        return response.json()

    def fetch_from_api(self, endpoint):
        response = requests.get(self.api_url + endpoint)
        return response.json()

    def fetch_from_api_and_insert_to_db(self, endpoint):
        # Запит до API
        response = requests.get(self.api_url + endpoint)
        api_data = response.json()

        # Запис у SQL базу даних
        insert_query = "INSERT INTO api_data (api_id, name, data) VALUES (%s, %s, %s)"
        with self.db.cursor() as cursor:
            for item in api_data:
                cursor.execute(
                    insert_query,
                    (item["id"], item["name"], json.dumps(item.get("data", {}))),
                )
            self.db.commit()

        return api_data

    def get_all_objects(self):
        return self.fetch_from_api("objects")

    def get_objects_by_ids(self, ids):
        ids_query = "&".join([f"id={id}" for id in ids])
        return self.fetch_from_api(f"objects?{ids_query}")

    def get_single_object(self, object_id):
        return self.fetch_from_api(f"objects/{object_id}")

    def send_to_db(self, query, args=None):
        with self.db.cursor() as cursor:
            cursor.execute(query, args)
            self.db.commit()

    def fetch_from_db(self, query, args=None):
        with self.db.cursor() as cursor:
            cursor.execute(query, args)
            return cursor.fetchall()

    def close(self):
        self.db.close()

    def add_object(self, data):
        response = requests.post(self.api_url + "objects", json=data)
        return response.json()

    def update_object_in_db(self, object_id, name, data):
        query = "UPDATE api_data SET name = %s, data = %s WHERE id = %s"
        args = (name, json.dumps(data), object_id)
        self.send_to_db(query, args)

    def update_full_object_in_db(self, object_id, new_name, new_data):
        query = "UPDATE api_data SET name = %s, data = %s WHERE id = %s"
        args = (new_name, json.dumps(new_data), object_id)
        self.send_to_db(query, args)

    def post_and_insert(self, endpoint, data):
        # POST request to API
        response = requests.post(self.api_url + endpoint, json=data)
        api_response = response.json()

        # INSERT into SQL
        insert_query = "INSERT INTO api_data (api_id, name, data) VALUES (%s, %s, %s)"
        self.send_to_db(
            insert_query,
            (
                api_response["id"],
                api_response["name"],
                json.dumps(api_response["data"]),
            ),
        )

        # SELECT to verify
        select_query = "SELECT * FROM api_data WHERE api_id = %s"
        db_response = self.fetch_from_db(select_query, (api_response["id"],))
        return db_response

    def put_and_update(self, object_id, endpoint, data):
        # PUT request to API
        response = requests.put(self.api_url + endpoint + f"/{object_id}", json=data)
        if response.status_code != 200:
            print(
                f"Response Body: {response.text}"
            )  # Додавання логування тіла відповіді
            raise Exception(
                f"API request failed with status code {response.status_code}"
            )

        # GET request to fetch updated data
        updated_response = requests.get(self.api_url + endpoint + f"/{object_id}")
        updated_data = updated_response.json()

        # Перевіряємо, чи відповідь від API містить необхідні поля
        if "name" not in updated_data or "data" not in updated_data:
            raise KeyError(
                "Required fields 'name' or 'data' are missing in the API response"
            )

        # UPDATE in SQL
        update_query = "UPDATE api_data SET name = %s, data = %s WHERE api_id = %s"
        self.send_to_db(
            update_query,
            (updated_data["name"], json.dumps(updated_data["data"]), object_id),
        )
