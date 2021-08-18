from functools import lru_cache
from typing import List, Tuple

from anki_swiss_knife.language_validator.chinese_characters_validator import ChineseCharacterValidator

chinese_validator = ChineseCharacterValidator()


def get_indexes_of_words_to_keep_in_phrase(
    phrase: str,
    words_to_keep: Tuple[str],
) -> Tuple[Tuple[str]]:
    list_of_index = []
    for name in words_to_keep:
        if name in phrase:
            start_index = phrase.index(name)
            end_index = start_index + (len(name) - 1)
            list_of_index.append(
                (
                    start_index,
                    end_index,
                )
            )
    return tuple(list_of_index)


@lru_cache()
def get_last_chinese_character_index(phrase: str, words_to_keep: List[str] = []) -> int:
    start_end_index = get_indexes_of_words_to_keep_in_phrase(phrase=phrase, words_to_keep=words_to_keep)
    for index, character in enumerate(phrase):
        if start_end_index and isinstance(start_end_index, Tuple):
            start, end = start_end_index
            if start >= index >= end:
                continue

        is_chinese = chinese_validator.is_chinese_character(character=character)
        if not is_chinese:
            return index
    return 0


def sanitize_phrase(phrase: str, text_to_remove: Tuple[str]) -> str:
    for text in text_to_remove:
        phrase = phrase.replace(text, "")
    return phrase
