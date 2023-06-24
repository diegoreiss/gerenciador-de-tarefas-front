import os
from configparser import ConfigParser


class ConfigIpAddress(ConfigParser):
    def get_ip_address(self, section: str = 'api'):
        parent_path = os.path.dirname(os.getcwd())
        full_file_path = os.path.join(parent_path, 'api.ini')

        self.read(full_file_path)

        if self.has_section(section):
            params = self.items(section)

            ini_params = {param[0]: param[1] for param in params}

            return ConfigIpAddress.__format_ip_address(ini_params)

    @staticmethod
    def __format_ip_address(params: dict):
        pattern = 'http://host:port'
        pattern_copy = pattern[:]

        for key, value in params.items():
            pattern_copy = pattern_copy.replace(key, value)

        return pattern_copy


IP_ADDRESS = ConfigIpAddress().get_ip_address()
