from unittest.mock import patch

import pytest

from anki_swiss_knife.anki_chinese_card_builder import AnkiChineseCardBuilder


def setup_anki_chinese_card_builder(file_to_convert=""):
    with patch("anki_swiss_knife.anki_chinese_card_builder.files.create_folder"):
        return AnkiChineseCardBuilder(file_to_convert=file_to_convert)


@pytest.mark.parametrize(
    "line, expected_result",
    [
        (
            "要 + V. (future tense) will, be going to + V.",
            "要 + V.;will, be going to + V.\n",
        ),
        (
            "放假 fàngjiǎ (v./n.) vacation",
            "放假;fàngjiǎ (v./n.) vacation\n",
        ),
        (
            "第一 + measure word, dìyī + measure first",
            "第一 + measure word;dìyī + measure first\n",
        ),
        (
            "No chinese Character",
            None,
        ),
        (
            "你吃午餐了吗？",
            None,
        ),
        (
            "六月开始变热",
            None,
        ),
        (
            "哪一季你最喜欢？nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?",
            "哪一季你最喜欢？;nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?\n",
        ),
        (
            "4个人一车 4 Gèrén yī chē 4 person in a car",
            "4个人一车;4 Gèrén yī chē 4 person in a car\n",
        ),
        (
            "12个人一队 12 ge rén yí duì 12 persons in a team",
            "12个人一队;12 ge rén yí duì 12 persons in a team\n",
        ),
        (
            "V. + 了 past tense (you did something)",
            "V. + 了;past tense (you did something)\n",
        ),
        (
            "你看过Harry Potter吗？Nǐ kànguò Harry Potter ma? Have you seen Harry Potter?",
            "你看过Harry Potter吗？;Nǐ kànguò Harry Potter ma? Have you seen Harry Potter?\n",
        ),
        (
            "今天(是)星期六 Jīntiān (shì) xīngqíliù Today is Saturday",
            "今天(是)星期六;Jīntiān (shì) xīngqíliù Today is Saturday\n",
        ),
    ],
)
def test__anki_chinese_card_builder__generator_row__should_return_expected_format(
    line,
    expected_result,
):
    anki_chinese_card_builder = setup_anki_chinese_card_builder()

    result = anki_chinese_card_builder.generate_row(line=line)
    assert result == expected_result


@pytest.mark.parametrize(
    "chinese_char, rest_of_sentence, expected_result",
    [
        (
            "哪一季你最喜欢？nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?",
            "nǎ yī jì nǐ zuì xǐhuān? Which season do you like best?",
            "Which season do you like best?",
        )
    ],
)
def test__anki_chinese_card_builder__extract_english_sentence__should_have_only_english(
    chinese_char,
    rest_of_sentence,
    expected_result,
):
    anki_chinese_card_builder = setup_anki_chinese_card_builder()
    result = anki_chinese_card_builder.extract_english_sentence(
        chinese_char=chinese_char, rest_of_sentence=rest_of_sentence
    )
    assert result == expected_result
