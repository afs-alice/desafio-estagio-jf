import requests


class RequestsModule():
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}

    def get_response(self, url: str) -> bytes:
        response = requests.get(url, headers=self.headers)
        return response.content
