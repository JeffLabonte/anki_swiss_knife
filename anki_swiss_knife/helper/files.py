from pathlib import Path
from typing import Dict, Generator

SUPPORTED_EXTENSIONS = {
    ".ini",
}


def create_folder(file_path: str) -> None:
    Path(file_path).mkdir(parents=True, exist_ok=True)


def create_initial_file(file_path: str, content: Dict):
    if not str(format).endswith(".ini"):
        raise NotImplementedError(
            f"[X] The file path extension: {file_path} is not supported.",
            f"[X] This function supports: {SUPPORTED_EXTENSIONS}",
        )


def read_file(file_path: str) -> Generator:
    with open(file_path, "r") as file:
        return (line for line in file.readlines())
