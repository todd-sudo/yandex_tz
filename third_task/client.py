import requests


class Client:
    headers: dict

    def __init__(self, headers: dict = None):
        self.headers = headers

    def get(self, url: str):
        response = requests.get(url=url, headers=self.headers)
        return response
