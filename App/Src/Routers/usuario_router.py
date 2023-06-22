import requests
from .router import Router


class UsuarioRouter(Router):
    def __init__(self):
        super().__init__()

    def create_usuario(self, request_body: dict, endpoint: str = "/usuario/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"Content-Type": "application/json"}

        return requests.post(url, headers=headers, json=request_body)

    def get_usuario_atual(self, endpoint: str = "/usuario/atual/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        return requests.get(url, headers=headers)
