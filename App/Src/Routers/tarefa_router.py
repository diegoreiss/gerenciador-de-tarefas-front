import requests
from requests.exceptions import InvalidURL
from .router import Router


class TarefaRouter(Router):
    def __init__(self):
        super().__init__()

    def get_tarefas_usuario_atual(self, endpoint: str = "/tarefa/usuario/atual/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.get(url, headers=headers)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def create_tarefa(self, data: dict, file: str, has_anexo: bool = False, endpoint: str = "/tarefa/"):
        url = f"{self._IP_ADDRESS}{endpoint}?has_anexo={has_anexo}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}
        files = {"file": open(file, "rb")} if has_anexo else None

        try:
            return requests.post(url, headers=headers, data=data, files=files)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def delete_tarefa(self, id: int, endpoint: str = "/tarefa/"):
        url = f"{self._IP_ADDRESS}{endpoint}{id}"
        headers = {"Authorization": f"{self._token_type} {self._token}"}

        try:
            return requests.delete(url, headers=headers)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def update_tarefa(self, id: int, data: dict, file: str, has_anexo: bool = False, endpoint: str = "/tarefa/"):
        url = f"{self._IP_ADDRESS}{endpoint}{id}?has_anexo={has_anexo}"
        headers = {"Authorization": f"{self._token_type} {self._token}"}
        files = {"file": open(file, "rb")} if has_anexo else None

        try:
            return requests.put(url, headers=headers, data=data, files=files)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e

    def download_tarefa(self, file_path: str, endpoint: str = "/tarefa/download/"):
        url = f"{self._IP_ADDRESS}{endpoint}"
        headers = {"accept": "application/json", "Authorization": f"{self._token_type} {self._token}"}
        params = {"file_path": file_path}

        try:
            return requests.get(url, headers=headers, params=params)
        except InvalidURL as e:
            raise e
        except BaseException as e:
            raise e
