import os
from pathlib import Path

PROJECT_NAME = "anki-swiss-knife"

CSV_DELIMITER = ";"

DEFAULT_ANKI_USER = "User 1"

COLLECTION_MEDIA_LINUX_PATH = os.path.join(Path.home(), ".local/share/Anki2/{anki_user}/collection.media/")

CONFIGURATION_FOLDER = os.path.join(Path.home(), f".config/{PROJECT_NAME}")
CONFIGURATION_FILE_INI = os.path.join(Path.home(), f".config/{PROJECT_NAME}/default.ini")
