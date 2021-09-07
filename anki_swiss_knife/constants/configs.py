import os
from pathlib import Path

from anki_swiss_knife.constants import base

CONFIGURATION_FOLDER = os.path.join(Path.home(), f".config/{base.PROJECT_NAME}")
CONFIGURATION_FILE_INI = os.path.join(Path.home(), f".config/{base.PROJECT_NAME}/default.ini")

DEFAULT_CONFIGURATIONS = {
    "General": {
        "text-with-speech": True,
        "swap-source-destination-language": True,
        "enable-google-docs": True,
        "enable-fluentu": False,
    },
    "FluentU": {
        "username": "",
        "password": "",
    },
    "GoogleDocs": {
        "credential_file": "",
        "document-id": "",
    },
}
