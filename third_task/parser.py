import aiohttp
import requests
from bs4 import BeautifulSoup

from client import Client


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,"
              "image/avif,image/webp,*/*;q=0.8",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:98.0) "
                  "Gecko/20100101 Firefox/98.0"
}
url = "https://vc.ru/new"


def get_last_news() -> dict:
    client = Client(headers=headers)
    response = client.get(url=url)
    soup = BeautifulSoup(response.text, "lxml")

    post_container = soup.find("div", class_="content-feed")
    link = post_container.find("a", class_="content-link").get("href")

    title = post_container.find(class_="content-title--short").text.strip()
    description = soup.find(class_="content-container")\
        .find_all(class_="l-island-a")
    if description is not None:
        description = description[1].text.strip()
    author = post_container.find(
        class_="content-header-author__name"
    ).text.strip()
    create_at = post_container.find("time").text.strip()

    last_news = {
        "title": title,
        "description": description,
        "create_at": create_at,
        "author": author,
        "link": link,
    }
    return last_news
