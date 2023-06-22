import requests
from requests.exceptions import InvalidURL
from .router import Router


class UsuarioRouter(Router):
    def __init__(self):
        super().__init__()

    def create_usuario(self, request_body: dict, endpoint: str = "/usuario/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"Content-Type": "application/json"}

        try:
            return requests.post(url, headers=headers, json=request_body)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def get_usuario_atual(self, endpoint: str = "/usuario/atual/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.get(url, headers=headers)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e
