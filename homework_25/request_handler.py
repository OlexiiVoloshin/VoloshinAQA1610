import requests
import logging


class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.INFO)

    def send_request(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
        except requests.exceptions.HTTPError as errh:
            self.logger.error(f"HTTP Error: {errh}")
            raise
        except requests.exceptions.ConnectionError as errc:
            self.logger.error(f"Error Connecting: {errc}")
            raise
        except requests.exceptions.Timeout as errt:
            self.logger.error(f"Timeout Error: {errt}")
            raise
        except requests.exceptions.RequestException as err:
            self.logger.error(f"Something went wrong: {err}")
            raise
        return response

    def create_and_delete_user(self, create_url, delete_url, user_data):
        # Створення об'єкта
        create_response = self.send_request("POST", create_url, data=user_data)
        if create_response.status_code == 201:
            self.logger.info("Об’єкт успішно створено.")
            created_user = create_response.json()

            # Видалення об'єкта
            delete_response = self.send_request(
                "DELETE", delete_url.format(created_user["id"])
            )
            if delete_response.status_code == 204:
                self.logger.info("Об’єкт успішно видалено.")
            else:
                self.logger.error("Помилка при видаленні об’єкта.")
        else:
            self.logger.error("Помилка при створенні об’єкта.")
