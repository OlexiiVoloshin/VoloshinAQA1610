import requests
import logging


class RequestHandler:
    def __init__(self):
        self.session = requests.Session()
        self.logger = logging.getLogger(__name__)

    def send_request(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            # Додав логування для успішного запиту
            self.logger.info(f"Запит до {url} успішно завершено.")
            return response  # Повертаю об'єкт відповіді для подальшої обробки
        except requests.exceptions.HTTPError as errh:
            self.logger.error(f"HTTP помилка: {errh}")
            return None
