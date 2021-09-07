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

    ```ini
    [DEFAULT]
    config_a = 1

    [GROUP_A]
    config_b = valueB
    ```
    """
    from anki_swiss_knife.helper.files import create_folder, get_parent_from_path

    folder_path = get_parent_from_path(
        file_path=file_path,
    )
    create_folder(
        folder_path=folder_path,
    )
    config = configparser.ConfigParser()
    for key, sub_dict in content.items():
        config[key] = {subkey: str(value) for subkey, value in sub_dict.items()}

    with open(file_path, "w+") as init_file:
        config.write(init_file)
