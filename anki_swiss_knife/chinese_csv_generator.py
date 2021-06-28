import re
from typing import List, Optional


class ChineseCSVGenerator:
    """
    Generate rows formatted for CSV. Using `;` as its delimiter

    This class works only for chinese character
    """
    TEXT_TO_KEEP_IN_FIRST_COLUMN = (
        " + V.",
        "+V.",
        " + measure word",
        "+measure word",
    )

    TEXT_TO_REMOVE = (
        "(future tense)",
    )

    CHINESE_UNICODES = "[\u4e00-\u9FFF]"
    LATIN_UNICODES = "[\u0000-\u007F]"

    def __init__(self, file_to_convert: str, extra_rules: Optional[List[str]] = None):
        self.file_to_convert = file_to_convert
        self.extra_rules = extra_rules

    def _is_character_in_unicode(self, unicode_regex, character):
        return getattr(re.search(unicode_regex, character), "endpos", 0) != 0

    def _remove_unwanted_text(self, text: str) -> str:
        text = text.lstrip(",").lstrip(" ")
        for remove in self.TEXT_TO_REMOVE:
            text = text.replace(remove, "").lstrip(" ")
        return text

    def _find_end_index_for_text_to_keep(self, text: str) -> List[int]:
        return [
            text.index(text_to_keep) + len(text_to_keep)
            for text_to_keep in self.TEXT_TO_KEEP_IN_FIRST_COLUMN
            if text_to_keep in text
        ]

    def _find_end_index_for_chinese_char(self, text: str) -> int:
        for index, character in enumerate(text):
            if self._is_character_in_unicode(
                unicode_regex=self.LATIN_UNICODES,
                character=character,
            ):
                return index

    def find_first_column_ends(self, text: str) -> int:
        indexes = self._find_end_index_for_text_to_keep(text=text)
        if indexes:
            indexes.sort(reverse=True)
            return indexes[0]
        else:
            return self._find_end_index_for_chinese_char(text=text)

    def has_chinese_charater_in_line(self, line: str) -> bool:
        chinese_chars = [
            character
            for character in line
            if self._is_character_in_unicode(
                unicode_regex=self.CHINESE_UNICODES,
                character=character,
            )
        ]
        return chinese_chars != []

    def has_latin_character_in_line(self, line: str):
        latin_chars = [
            character
            for character in line
            if self._is_character_in_unicode(
                unicode_regex=self.LATIN_UNICODES,
                character=character,
            )
        ]
        return latin_chars != []

    def generate_row(self, line: str) -> Optional[str]:
        if not self.has_chinese_charater_in_line(line=line) or not self.has_latin_character_in_line(line=line):
            return None

        index = self.find_first_column_ends(text=line)

        chinese_chars = self._remove_unwanted_text(text=line[0:index])
        rest_of_sentence = self._remove_unwanted_text(text=line[index:])

        return f"{chinese_chars};{rest_of_sentence}"

    def generate_csv(self):
        file_content = self._read_file()
        with open(self._generate_csv_file_path(), "w+") as f:
            for content in file_content:
                row = self.generate_row(line=content)
                if row:
                    f.write(row)

    def _read_file(self):
        with open(self.file_to_convert, "r") as f:
            return f.readlines()

    def _generate_csv_file_path(self) -> str:
        return f"{self.file_to_convert.split('.')[0]}.csv"
