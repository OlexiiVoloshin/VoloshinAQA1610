import requests
import pytest
import json
from homework_25.request_handler import RequestHandler


class TestAPI:
    @pytest.fixture(autouse=True)
    def setup_session(self):
        self.session = requests.Session()
        yield
        self.session.close()
        # Позитивні тести

    def test_positive_get(self):
        # Тестування GET-запиту для отримання списку користувачів
        response = self.session.get("https://reqres.in/api/users?page=2")
        print(
            f"Відповідь JSON для test_positive_get: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_get_single_user(self):
        # Тестування GET-запиту для отримання одного користувача
        response = self.session.get("https://reqres.in/api/users/2")
        print(
            f"Відповідь JSON для test_positive_get_single_user: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_get_list_resource(self):
        # Тестування GET-запиту для отримання списку ресурсів
        response = self.session.get("https://reqres.in/api/unknown")
        print(
            f"Відповідь JSON для test_positive_get_list_resource: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_get_single_resource(self):
        # Тестування GET-запиту для отримання одного ресурсу
        response = self.session.get("https://reqres.in/api/unknown/2")
        print(
            f"Відповідь JSON для test_positive_get_single_resource: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_get_delayed_response(self):
        # Тестування GET-запиту з відстроченою відповіддю
        response = self.session.get("https://reqres.in/api/users?delay=3")
        print(
            f"Відповідь JSON для test_positive_get_delayed_response: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_post_create(self):
        # Тестування POST-запиту для створення користувача
        response = self.session.post(
            "https://reqres.in/api/users", data={"name": "morpheus", "job": "leader"}
        )
        print(
            f"Відповідь JSON для test_positive_post_create: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 201, "Очікуваний статус-код 201"

    def test_positive_post_login_successful(self):
        # Тестування POST-запиту для успішного входу в систему
        response = self.session.post(
            "https://reqres.in/api/login",
            data={"email": "eve.holt@reqres.in", "password": "cityslicka"},
        )
        print(
            f"Відповідь JSON для test_positive_post_login_successful: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_put_update(self):
        # Тестування PUT-запиту для оновлення даних користувача
        response = self.session.put(
            "https://reqres.in/api/users/2",
            data={"name": "morpheus", "job": "zion resident"},
        )
        print(
            f"Відповідь JSON для test_positive_put_update: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"

    def test_positive_patch_update(self):
        # Тестування PATCH-запиту для часткового оновлення даних користувача
        response = self.session.patch(
            "https://reqres.in/api/users/2",
            data={"name": "morpheus", "job": "zion resident"},
        )
        print(
            f"Відповідь JSON для test_positive_patch_update: {json.dumps(response.json(), indent=4)}"
        )
        assert response.status_code == 200, "Очікуваний статус-код 200"


class TestRequestHandler:
    @pytest.fixture(autouse=True)
    def setup(self):
        # Ініціалізація RequestHandler для тестів
        self.request_handler = RequestHandler()

    def test_create_and_delete_user(self):
        create_url = "https://reqres.in/api/users"
        delete_url = "https://reqres.in/api/users/{}"
        user_data = {"name": "morpheu", "job": "leader"}
        # Тестування функціональності створення та видалення користувача в RequestHandler
        self.request_handler.create_and_delete_user(create_url, delete_url, user_data)
