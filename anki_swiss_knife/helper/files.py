import os


def create_folder(file_path: str):
    if not os.path.exists(file_path):
        os.mkdir(file_path)
