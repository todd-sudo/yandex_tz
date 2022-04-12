from client import Client
from parser import get_last_news
from config import get_token_bot


def send_news_channel(channel_name: str):
    """ Отправляет последний пост в телеграм канал
    """
    client = Client()
    last_news = get_last_news()

    message_text = """
Ссылка: {0}

Автор: {1}

Создано: {2}

Название: {3}

Описание: {4}
    """.format(
        last_news.get("link"),
        last_news.get("author"),
        last_news.get("create_at"),
        last_news.get("title"),
        last_news.get("description"),
    )

    tg_url = f"https://api.telegram.org/bot{get_token_bot()}" \
             f"/sendMessage?chat_id=@{channel_name}&text={message_text}"
    response = client.get(url=tg_url)
    if response.status_code != 200:
        raise Exception(f"Status code {response.status_code} != 200")
