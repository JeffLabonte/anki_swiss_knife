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
