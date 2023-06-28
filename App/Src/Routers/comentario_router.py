import requests
from requests.exceptions import InvalidURL
from .router import Router


class ComentarioRouter(Router):
    def __init__(self):
        super().__init__()

    def get_comentarios_by_id_tarefa(self, tarefa_id: int, endpoint: str = "/comentario/"):
        url = f"{self._IP_ADDRESS}{endpoint}{tarefa_id}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.get(url, headers=headers)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def create_comentario(self, request_body: dict, endpoint: str = "/comentario/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.post(url, headers=headers, json=request_body)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def update_comentario(self, id: int, request_body: dict, endpoint: str = "/comentario/"):
        url = f"{self._IP_ADDRESS}{endpoint}{id}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.put(url, headers=headers, json=request_body)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def delete_comentario(self, id: int, endpoint: str = "/comentario/"):
        url = f"{self._IP_ADDRESS}{endpoint}{id}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.delete(url, headers=headers)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e
