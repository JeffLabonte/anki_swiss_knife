from collections import namedtuple
from typing import List, Set, Tuple

from anki_swiss_knife.constants.languages import EXTRA_PUNCTUATION_TO_KEEP
from anki_swiss_knife.language_validator.chinese_characters_validator import (
    ChineseCharacterValidator,
)

chinese_validator = ChineseCharacterValidator()

WordPosition = namedtuple("WordPosition", ["start_index", "end_index"])


def get_indexes_of_words_to_keep_in_phrase(
    phrase: str,
    words_to_keep: Set[str],
) -> List[WordPosition]:
    list_of_index = []
    for name in words_to_keep:
        if name in phrase:
            start_index = phrase.index(name)
            end_index = start_index + (len(name) - 1)
            list_of_index.append(
                WordPosition(
                    start_index=start_index,
                    end_index=end_index,
                )
            )
    return list_of_index


def get_last_chinese_character_index(phrase: str, words_to_keep: Set[str]) -> int:
    word_positions = get_indexes_of_words_to_keep_in_phrase(phrase=phrase, words_to_keep=words_to_keep)
    index = 0
    for index, character in enumerate(phrase):
        if word_positions:
            if any(
                int(word_position.start_index) >= index or index <= int(word_position.end_index)
                for word_position in word_positions
            ):
                continue

        is_chinese = (
            chinese_validator.is_chinese_character(character=character)
            or character in EXTRA_PUNCTUATION_TO_KEEP
            or (character.isdigit() and chinese_validator.is_chinese_character(phrase[index:]))
        )
        if not is_chinese:
            return index
    return index + 1


def sanitize_phrase(phrase: str, text_to_remove: Tuple[str]) -> str:
    for text in text_to_remove:
        phrase = phrase.replace(text, "")
    return phrase
