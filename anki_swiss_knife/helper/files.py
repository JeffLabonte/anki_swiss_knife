import os
from typing import Generator


def create_folder(file_path: str) -> None:
    if not os.path.exists(file_path):
        os.mkdir(file_path)


def read_file(file_path: str) -> Generator:
    with open(file_path, "r") as file:
        return (line for line in file.readlines())
