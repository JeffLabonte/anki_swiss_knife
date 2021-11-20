from unittest.mock import MagicMock, patch

import pytest


def setup_anki_chinese_card_builder(file_to_convert=""):
    from anki_swiss_knife.anki_chinese_card_builder import AnkiChineseCardBuilder

    with patch("anki_swiss_knife.anki_chinese_card_builder.files.create_folder"):
        anki_chinese_card_builder = AnkiChineseCardBuilder(file_to_convert=file_to_convert)
        anki_chinese_card_builder.get_translation = MagicMock(return_value="No Service Available")
        return anki_chinese_card_builder


@pytest.mark.parametrize(
    "line, expected_chinese, expected_pinyin, expected_notes",
    [
        (
            "要 + V. (future tense) yào will, be going to + V.",
            "要 + V.",
            "yào",
            "yào will, be going to + V.",
        ),
        (
            "第一 + measure word, dì yī + measure word first",
            "第一 + measure word,",
            "dì yī",
            "dì yī + measure word first",
        ),
        ("No chinese Character", None, None, None),
        (
            "你吃午餐了吗？",
            "你吃午餐了吗？",
            "nǐ chī wǔ cān le ma ？",
            "",
        ),
        (
            "六月开始变热",
            "六月开始变热",
            "liù yuè kāi shǐ biàn rè",
            "",
        ),
        (
            "哪一季你最喜欢？nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?",
            "哪一季你最喜欢？",
            "nǎ yī jì nǐ zuì xǐ huān ？",
            "nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?",
        ),
        (
            "4个人一车 4 Gèrén yī chē 4 person in a car",
            "4个人一车",
            "4 gè rén yī chē",
            "4 Gèrén yī chē 4 person in a car",
        ),
    ],
)
def test__anki_chinese_card_builder__generator_row__should_return_expected_format(
    line,
    expected_chinese,
    expected_pinyin,
    expected_notes,
):
    anki_chinese_card_builder = setup_anki_chinese_card_builder()

    result = anki_chinese_card_builder.generate_anki_card(line=line)
    if result is not None:
        assert result.chinese_character == expected_chinese
        assert result.notes == expected_notes
        assert result.pinyin == expected_pinyin
        assert result.translation == "No Service Available"
    else:
        assert expected_chinese is None
        assert expected_pinyin is None
        assert expected_notes is None
