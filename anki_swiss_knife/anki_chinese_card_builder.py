import re
from typing import Optional

from xpinyin import Pinyin

from anki_swiss_knife.anki.anki_card import ChineseAnkiCard
from anki_swiss_knife.constants import file_paths
from anki_swiss_knife.constants.languages import CHINESE_TEXT_TO_REMOVE, CHINESE_WORDS_TO_KEEP
from anki_swiss_knife.helper import files
from anki_swiss_knife.language_extractors import get_last_chinese_character_index, sanitize_phrase
from anki_swiss_knife.translation import translate_text

ENGLISH_TEXT_REGEX = re.compile(r"[a-zA-Z1-9+.,' ]+[?! ]?")


class AnkiChineseCardBuilder:
    """
    Generate rows formatted for CSV. Using `;` as its delimiter

    This class works only for chinese character
    """

    SOURCE_LANGUAGE = "zh"
    TARGET_LANGUAGE = "en"

    def __init__(self, file_to_convert: str, is_chinese_first_column: bool = True):
        self.file_to_convert = file_to_convert
        self.csv_output_path = self._generate_csv_file_path()
        self.is_chinese_first_column = is_chinese_first_column
        self.pinyin = Pinyin()
        files.create_folder("/".join(self.csv_output_path.split("/")[:-1]))

    @staticmethod
    def _line_is_valid(line: str):
        return not line.startswith("#")

    def get_pinyin(self, chinese_chars) -> str:
        words_to_remove = list(CHINESE_WORDS_TO_KEEP) + [","]
        return sanitize_phrase(
            phrase=self.pinyin.get_pinyin(chars=chinese_chars, splitter=" ", tone_marks="marks"),
            text_to_remove=words_to_remove,
        ).rstrip()

    def get_translation(self, chinese_chars):
        return translate_text(
            text_to_translate=chinese_chars,
            source_language_code=self.SOURCE_LANGUAGE,
            target_language_code=self.TARGET_LANGUAGE,
        )

    def generate_anki_card(self, line: str) -> Optional[ChineseAnkiCard]:
        sanitized_phrase = sanitize_phrase(phrase=line, text_to_remove=CHINESE_TEXT_TO_REMOVE)
        index = get_last_chinese_character_index(phrase=sanitized_phrase, words_to_keep=CHINESE_WORDS_TO_KEEP)
        chinese_phrase, notes = sanitized_phrase[:index], sanitized_phrase[index:].lstrip()

        if chinese_phrase:
            return ChineseAnkiCard(
                chinese_character=chinese_phrase,
                pinyin=self.get_pinyin(chinese_chars=chinese_phrase),
                translation=self.get_translation(chinese_chars=chinese_phrase),
                notes=notes,
            )

    def generate_csv(self) -> str:
        file_content = files.read_file(self.file_to_convert)
        with open(self.csv_output_path, "w+") as f:
            for content in file_content:
                if self._line_is_valid(line=content) and (anki_card := self.generate_anki_card(line=content)):
                    f.write(anki_card.to_csv(is_chinese_first=self.is_chinese_first_column))

            return self.csv_output_path

    def _generate_csv_file_path(self) -> str:
        tmp_csv_file_path = self.file_to_convert.replace(file_paths.GOOGLE_DOC_FOLDER_NAME, file_paths.CSV_FOLDER_NAME)
        return f"{tmp_csv_file_path.split('.')[0]}.csv"
