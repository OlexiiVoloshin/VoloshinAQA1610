import requests
import pytest
import json


class TestAPI:
    @pytest.fixture(autouse=True)
    def setup_session(self):
        # Ініціалізація сесії для кожного тесту
        self.session = requests.Session()

    def teardown_session(self):
        # Використання функції finalization pytest для закриття сесії після кожного тесту
        yield
        self.session.close()

    # Негативні тести
    def test_negative_post_register_unsuccessful(self):
        # Тест POST-запиту для неуспішної реєстрації
        response = self.session.post(
            "https://reqres.in/api/register", data={"email": "sydneyfife"}
        )
        print(
            f"Відповідь JSON для test_negative_post_register_unsuccessful: {json.dumps(response.json(), indent=4)}"
        )
        assert (
            response.status_code == 400
        ), f"Очікуваний статус-код 400, отримано {response.status_code}"

    def test_negative_post_login_unsuccessful(self):
        # Тест POST-запиту для неуспішного входу в систему
        response = self.session.post(
            "https://reqres.in/api/login", data={"email": "peterklaven"}
        )
        print(
            f"Відповідь JSON для test_negative_post_login_unsuccessful: {json.dumps(response.json(), indent=4)}"
        )
        assert (
            response.status_code == 400
        ), f"Очікуваний статус-код 400, отримано {response.status_code}"

    def test_negative_get_with_invalid_page(self):
        # Тест GET-запиту з недійсним номером сторінки
        response = self.session.get("https://reqres.in/api/users?page=999")
        print(
            f"Відповідь JSON для test_negative_get_with_invalid_page: {json.dumps(response.json(), indent=4)}"
        )
        assert (
            response.status_code == 200
        ), f"Очікуваний статус-код 200, отримано {response.status_code}"
        assert response.json()["data"] == [], "Очікувано пустий список даних"

    def test_negative_get_single_user_not_found(self):
        # Тест GET-запиту для неіснуючого користувача
        response = self.session.get("https://reqres.in/api/users/999")
        print(
            f"Відповідь JSON для test_negative_get_single_user_not_found: {json.dumps(response.json(), indent=4)}"
        )
        assert (
            response.status_code == 404
        ), f"Очікуваний статус-код 404, отримано {response.status_code}"

    def test_negative_get_single_resource_not_found(self):
        # Тест GET-запиту для неіснуючого ресурсу
        response = self.session.get("https://reqres.in/api/unknown/999")
        print(
            f"Відповідь JSON для test_negative_get_single_resource_not_found: {json.dumps(response.json(), indent=4)}"
        )
        assert (
            response.status_code == 404
        ), f"Очікуваний статус-код 404, отримано {response.status_code}"
