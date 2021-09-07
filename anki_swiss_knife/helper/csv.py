import csv
from typing import List

from anki_swiss_knife.anki.card_with_speech import CardWithSpeech
from anki_swiss_knife.constants import base


def read_csv(file_path):
    if ".csv" not in file_path:
        raise RuntimeError("File extension is not .csv")

    with open(file_path, "r") as csv_file:
        return [CardWithSpeech(*row) for row in csv.reader(csv_file, delimiter=base.CSV_DELIMITER) if row]


def write_csv(contents: List, file_path: str) -> None:
    with open(file_path, "w+") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=base.CSV_DELIMITER)
        for content in contents:
            if getattr(content, "to_list"):
                csv_writer.writerow(content.to_list())
            else:
                csv_writer.writerow(content.split(base.CSV_DELIMITER))
