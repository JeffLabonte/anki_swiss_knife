import configparser
from typing import Dict


def create_ini_file(file_path: str, content: Dict) -> None:
    """
    Expected format for content:

    ```json
    {
        "DEFAULT": {
            "config_a": 1
        },
        "GROUP_A": {
            "config_b": "valueB"
        }
    }
    ```
    result:
    [DEFAULT]
    config_a = 1

    [GROUP_A]
    config_b = valueB
    """
    config = configparser.ConfigParser()
    for key, value in content:
        config[key] = str(value)

    with open(file_path, "w+") as init_file:
        config.write(init_file)
