import re
from typing import List, Optional, Tuple


class CSVGenerator:
    ADD_RULES = [
        " + V",
        "+V"
    ]

    def __init__(self, file_to_convert: str, extra_rules: Optional[List[str]] = None):
        self.file_to_convert = file_to_convert
        self.extra_rules = extra_rules

    def _is_chinese_character(self, character):
        is_chinese = False
        if re.search("[\u4e00-\u9FFF]", character):
            is_chinese = not is_chinese
        return is_chinese

    def generate_row(self, line: str) -> Tuple:
        content_words = line.split(" ")
        rest_of_sentense = " ".join(content_words[1:])
        chinese_chars = content_words[0].strip(" ")
        return chinese_chars, rest_of_sentense

    def generate_csv(self):
        file_content = self._read_file()
        with open(self._generate_csv_file_path(), "w+") as f:
            for content in file_content:
                chinese_chars, rest_of_sentense = self.generate_row(line=content)
                if chinese_chars and rest_of_sentense:
                    f.write(f"{chinese_chars};{rest_of_sentense}")

    def _read_file(self):
        with open(self.file_to_convert, "r") as f:
            return f.readlines()

    def _generate_csv_file_path(self) -> str:
        return f"{self.file_to_convert.split('.')[0]}.csv"

