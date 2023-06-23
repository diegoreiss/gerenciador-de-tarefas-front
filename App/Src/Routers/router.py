import os
from .config_ip import IP_ADDRESS


class Router:
    def __init__(self):
        self._IP_ADDRESS = IP_ADDRESS
        self._token = os.environ.get("TOKEN_USUARIO")
        self._token_type = os.environ.get("TOKEN_USUARIO_TYPE")
