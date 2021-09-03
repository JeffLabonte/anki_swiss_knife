from typing import Dict


class ConfigManager:
    def __init__(self) -> None:
        self._config = self._retrieve_config()

    def _retrieve_config(self):
        pass

    @property
    def config(self) -> Dict:
        return self._config
