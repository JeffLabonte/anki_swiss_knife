import os
from pathlib import Path
from typing import Dict, Generator, Optional

from anki_swiss_knife.helper.ini_file import create_ini_file

SUPPORTED_EXTENSIONS = {
    "ini": create_ini_file,
}


def create_folder(file_path: str) -> None:
    Path(file_path).mkdir(parents=True, exist_ok=True)


def get_file_extension(file_path: str) -> Optional[str]:
    if file_extension := file_path.split("."):
        return file_extension[-1]


def create_initial_file(file_path: str, content: Dict, force: bool = False):
    file_extension = get_file_extension(file_path=file_path)
    if not any(file_extension == extension for extension in SUPPORTED_EXTENSIONS.keys()):
        raise NotImplementedError(
            f"[X] The file path extension: {file_path} is not supported.",
            f"[X] This function supports: {SUPPORTED_EXTENSIONS}",
        )

    if force or not os.path.exists(file_path):
        SUPPORTED_EXTENSIONS[file_extension](
            file_path=file_path,
            content=content,
        )


def read_file(file_path: str) -> Generator:
    with open(file_path, "r") as file:
        return (line for line in file.readlines())
