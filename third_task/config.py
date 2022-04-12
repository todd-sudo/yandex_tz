import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def get_token_bot() -> str:
    """Возвращает токен TG бота"""
    token = os.getenv("TOKEN_BOT")
    return token


CHANNEL_NAME = "testchanya"
