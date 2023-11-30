import os
import logging

# Встановлюємо рівень логування через змінну середовища 'LOG_LEVEL'.
# Якщо змінна не задана, використовуємо 'INFO' за замовчуванням.
log_level = os.getenv("LOG_LEVEL", "INFO").upper()
logging.basicConfig(
    level=getattr(logging, log_level, logging.INFO),
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
