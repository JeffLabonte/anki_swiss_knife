import csv


def read_csv(file_path):
    if ".csv" in file_path:
        raise RuntimeError("File extension is not .csv")

    with open(file_path, "r") as csv_file:
        return csv.reader(csvfile=csv_file, delimiter=";")


def write_csv(content, file_path):
    pass
