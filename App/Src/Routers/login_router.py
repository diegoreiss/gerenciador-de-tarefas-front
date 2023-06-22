import requests
from .router import Router


class LoginRouter(Router):
    def __init__(self):
        super().__init__()

    def login(self, data: dict, endpoint: str = "/login"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        return requests.post(url, headers=headers, data=data)
