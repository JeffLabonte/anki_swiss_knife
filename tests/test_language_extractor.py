from anki_swiss_knife.constants.languages import CHINESE_TEXT_TO_REMOVE
from anki_swiss_knife import language_extractors
import pytest


@pytest.mark.parametrize(
    "multi_language_phrase, expected_index, expected_chinese",
    [
        (
            "你吃什么？something",
            5,
            "你吃什么？",
        ),
        (
            "我吃苹果 something to wrote",
            4,
            "我吃苹果",
        ),
        (
            "我学中文。a phrase",
            5,
            "我学中文。",
        ),
        (
            "我吃蓝莓及，也喝咖啡非 We write another sentence",
            11,
            "我吃蓝莓及，也喝咖啡非",
        ),
    ],
)
def test__language_extractors__get_last_chinese_character_index(
    multi_language_phrase: str,
    expected_index: int,
    expected_chinese: str,
):
    index = language_extractors.get_last_chinese_character_index(phrase=multi_language_phrase)
    assert multi_language_phrase[:index] == expected_chinese
    assert index == expected_index


def test__language_extractors__sanitize_phrase():
    phrase = "我要说 (future tense) 我吃一个苹果"
    expected_sanitized_phrase = "我要说  我吃一个苹果"
    sanitized_phrase = language_extractors.sanitize_phrase(
        phrase=phrase,
        text_to_remove=CHINESE_TEXT_TO_REMOVE,
    )
    assert sanitized_phrase == expected_sanitized_phrase
