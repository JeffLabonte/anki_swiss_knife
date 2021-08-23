import os
from pathlib import Path

from anki_swiss_knife.constants import base

DEFAULT_BASE_FOLDER = os.path.join(Path.home(), base.PROJECT_NAME)

CSV_FOLDER_NAME = "csv"
GOOGLE_DOC_FOLDER_NAME = "gdoc"
