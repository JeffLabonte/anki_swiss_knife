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
            "放假 (v./n.) fàng jiǎ (v./n.) vacation",
            "放假 (v./n.)",
            "fàng jiǎ",
            "fàng jiǎ (v./n.) vacation",
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
        # (
        #     "12个人一队 12 ge rén yí duì 12 persons in a team",
        #     "12个人一队;12 gè rén yī duì\n12 persons in a team\n",
        # ),
        # (
        #     "V. + 了 past tense (you did something)",
        #     "V. + 了;le\nyou did something\n",
        # ),
        # (
        #     "你看过Harry Potter吗？Nǐ kànguò Harry Potter ma? Have you seen Harry Potter?",
        #     "你看过Harry Potter吗？;nǐ kàn guò Harry Potter ma ？\nHave you seen Harry Potter?\n",
        # ),
        # (
        #     "今天(是)星期六 Jīntiān (shì) xīngqíliù Today is Saturday",
        #     "今天(是)星期六;jīn tiān xīng qī liù\nToday is Saturday\n",
        # ),
        # (
        #     "今天天气怎么样？ jīn tiān tiān qì zěn me yáng ？ How's the weather today?",
        #     "今天天气怎么样？;jīn tiān tiān qì zěn me yáng ？\nHow's the weather today?\n",
        # ),
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
