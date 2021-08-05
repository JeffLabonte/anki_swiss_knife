import re
from typing import List, Optional

from xpinyin import Pinyin

from anki_swiss_knife import translation
from anki_swiss_knife.anki.anki_card import ChineseAnkiCard
from anki_swiss_knife.constants import file_paths
from anki_swiss_knife.helper import files
from anki_swiss_knife.language_validator.chinese_characters_validator import ChineseCharacterValidator

ENGLISH_TEXT_REGEX = re.compile(r"[a-zA-Z1-9+.,' ]+[?! ]?")


class AnkiChineseCardBuilder:
    """
    Generate rows formatted for CSV. Using `;` as its delimiter

    This class works only for chinese character
    """

    TEXT_TO_KEEP = (
        " + V.",
        "+ V.",
        "+V.",
        " + measure word",
        "+ measure word",
        "+measure word",
        "SF",
        "Quebec City",
        " + W",
        "V. + ",
        "(个)",
        "Harry Potter",
        "Star Wars",
        "+someone.+",
        "Ajd. / V.  + ",
        "(是)",
        "，",
        "(v./n.)",
    )

    NAMES = {
        "Harry Potter",
        "SF",
        "Quebec City",
        "Star Wars",
    }

    TEXT_TO_REMOVE = ("(future tense)",)

    def __init__(self, file_to_convert: str, is_chinese_first_column: bool = True):
        self.file_to_convert = file_to_convert
        self.csv_output_path = self._generate_csv_file_path()
        self.is_chinese_first_column = is_chinese_first_column
        self.validator = ChineseCharacterValidator()
        self.pinyin = Pinyin()
        files.create_folder("/".join(self.csv_output_path.split("/")[:-1]))

    def _remove_unwanted_text(self, text: str) -> str:
        text = text.lstrip(",").lstrip(" ")
        for remove in self.TEXT_TO_REMOVE:
            text = text.replace(remove, "").lstrip(" ")
        return text

    def _find_text_to_keep_index_from_phrase(self, phrase: str) -> List[int]:
        return [
            phrase.index(text_to_keep) + len(text_to_keep)
            for index, text_to_keep in enumerate(self.TEXT_TO_KEEP)
            if text_to_keep in phrase
        ]

    def _find_end_index_for_chinese_char(self, text: str) -> int:
        for index, character in enumerate(text):
            if (
                self.validator.is_latin_character(
                    character=character,
                )
                and not character.isdigit()
            ):
                return index

    def find_first_column_ends(self, text: str) -> int:
        indexes = self._find_text_to_keep_index_from_phrase(phrase=text)
        if indexes:
            indexes.sort(reverse=True)
            first_column_index = indexes[0]
            for index, character in enumerate(text[first_column_index:]):
                if self.validator.is_latin_character(
                    character=character,
                ):
                    return first_column_index + index

        return self._find_end_index_for_chinese_char(text=text)

    def remove_text_to_keep(self, characters_to_sanitize: str) -> str:
        for character_to_remove in self.TEXT_TO_KEEP:
            if character_to_remove not in self.NAMES:
                characters_to_sanitize = characters_to_sanitize.replace(character_to_remove, "")
        return characters_to_sanitize

    def split_english_and_pinyin(self, chinese_char: str, rest_of_sentence: str) -> str:
        sanitized_chinese_char = self.remove_text_to_keep(characters_to_sanitize=chinese_char)

        unmarked_pinyin = self.pinyin.get_pinyin(sanitized_chinese_char).split("-")
        marked_pinyin = self.pinyin.get_pinyin(sanitized_chinese_char, tone_marks="marks").split("-")
        number_pinyin = self.pinyin.get_pinyin(sanitized_chinese_char, tone_marks="numbers").split("-")
        all_pinyins = marked_pinyin + number_pinyin + unmarked_pinyin

        english_translation = rest_of_sentence
        for pinyin in all_pinyins:
            if pinyin.isalpha():
                english_translation = english_translation.replace(pinyin, "")

        try:
            english_sentence = ENGLISH_TEXT_REGEX.findall(english_translation.strip("\n"))
            english_sentence = self.remove_text_to_keep(english_sentence[-1]).lstrip() if english_sentence else None

            if not english_sentence:
                english_sentence = translation.translate_text(
                    text_to_translate=chinese_char,
                    source_language_code="zh",
                    target_language_code="en",
                )

            return english_sentence, " ".join(marked_pinyin).rstrip()

        except IndexError as e:
            print(f"Something went wrong: {e}\nPinyin with english: {rest_of_sentence}\n")
            print(f"Pinyin Detected: {all_pinyins}")
            raise

    def generate_row(self, line: str) -> Optional[str]:
        if (
            not self.validator.has_chinese_character_in_line(line=line)
            or not self.validator.has_latin_character_in_line(line=line)
            or line.startswith("#")
        ):
            print(f"[-] This line doesn't work: {line}")
            return None

        index = self.find_first_column_ends(text=line)

        chinese_chars = self._remove_unwanted_text(line[0:index])
        english_translation, pinyin = self.split_english_and_pinyin(
            chinese_char=chinese_chars,
            rest_of_sentence=self._remove_unwanted_text(line[index:]),
        )
        chinese_anki_card = ChineseAnkiCard(
            chinese_character=chinese_chars,
            pinyin=pinyin,
            translation=english_translation,
        )

        return chinese_anki_card.to_csv(is_chinese_first=self.is_chinese_first_column)

    def generate_csv(self) -> str:
        file_content = files.read_file(self.file_to_convert)
        with open(self.csv_output_path, "w+") as f:
            for content in file_content:
                row = self.generate_row(line=content)
                if row and len(row) - 2 != len(content):
                    f.write(row)

            return self.csv_output_path

    def _generate_csv_file_path(self) -> str:
        tmp_csv_file_path = self.file_to_convert.replace(file_paths.GOOGLE_DOC_FOLDER_NAME, file_paths.CSV_FOLDER_NAME)
        return f"{tmp_csv_file_path.split('.')[0]}.csv"
