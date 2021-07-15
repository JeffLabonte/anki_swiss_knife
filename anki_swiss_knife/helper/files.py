from pathlib import Path
from typing import Generator


def create_folder(file_path: str) -> None:
    Path(file_path).mkdir(parents=True, exist_ok=True)


def read_file(file_path: str) -> Generator:
    with open(file_path, "r") as file:
        return (line for line in file.readlines())
