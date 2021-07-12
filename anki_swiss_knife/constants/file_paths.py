from pathlib import Path

PROJECT_NAME = "anki_swiss_knife"

DEFAULT_BASE_FOLDER = Path.joinpath(Path.home(), PROJECT_NAME)

CSV_FOLDER = Path.joinpath(f"{DEFAULT_BASE_FOLDER}", "csv")
GOOGLE_DOC_FOLDER = Path.joinpath(f"{DEFAULT_BASE_FOLDER}", "gdoc")
