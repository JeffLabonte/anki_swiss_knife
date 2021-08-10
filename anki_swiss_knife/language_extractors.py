from typing import Tuple
from anki_swiss_knife.language_validator.chinese_characters_validator import ChineseCharacterValidator
from functools import lru_cache


chinese_validator = ChineseCharacterValidator()


@lru_cache()
def get_last_chinese_character_index(phrase: str) -> int:
    for index, character in enumerate(phrase):
        is_chinese = chinese_validator.is_chinese_character(character=character)
        if not is_chinese:
            return index
    return 0


def sanitize_phrase(phrase: str, text_to_remove: Tuple[str]) -> str:
    for text in text_to_remove:
        phrase = phrase.replace(text, "")
    return phrase
