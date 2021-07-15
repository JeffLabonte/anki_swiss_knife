import csv
from typing import List

from anki_swiss_knife.constants import base


def read_csv(file_path):
    if ".csv" in file_path:
        raise RuntimeError("File extension is not .csv")

    with open(file_path, "r") as csv_file:
        return csv.reader(csvfile=csv_file, delimiter=base.CSV_DELIMITER)


def write_csv(contents: List, file_path: str) -> None:
    csv_writer = csv.writer(csvfile=file_path, delimiter=base.CSV_DELIMITER)
    for content in contents:
        if getattr(content, "to_list"):
            csv_writer.writerow(content.to_list())
        else:
            csv_writer.writerow(content.split(base.CSV_DELIMITER))
