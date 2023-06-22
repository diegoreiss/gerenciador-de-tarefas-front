import requests
from requests.exceptions import InvalidURL
from .router import Router


class LoginRouter(Router):
    def __init__(self):
        super().__init__()

    def login(self, data: dict, endpoint: str = "/login"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}

        try:
            return requests.post(url, headers=headers, data=data)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e
