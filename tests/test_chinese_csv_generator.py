import pytest

from anki_swiss_knife.chinese_csv_generator import ChineseCSVGenerator


def setup_csv_generator(file_to_convert=None):
    return ChineseCSVGenerator(file_to_convert=file_to_convert)


def test__csv_generator__is_chinese_character__should_return_true_on_chinese_char():
    csv_generator = setup_csv_generator()
    chinese_char = "也"
    assert csv_generator.has_chinese_charater_in_line(chinese_char) is True


def test__csv_generator__is_chinese_character__should_return_false_on_latin_char():
    csv_generator = setup_csv_generator()
    assert csv_generator.has_chinese_charater_in_line("a") is False


@pytest.mark.parametrize("line, expected_result", [
    ("要 + V. (future tense) will, be going to + V.", "要 + V.;will, be going to + V.",),
    ("放假 fàngjià (v./n.) vacation", "放假;fàngjià (v./n.) vacation"),
    ("第一 + measure word, dìyī + measure first", "第一 + measure word;dìyī + measure first"),
    ("No chinese Character", None),
    ("你吃午餐了吗？", None),
    (
        "哪一季你最喜欢？nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?",
        "哪一季你最喜欢？;nǎ yí jì nǐ zuì xǐhuān? Which season do you like best?",
    ),
])
def test__csv_generator__generator_row__should_return_expected_format(
    line,
    expected_result,
):
    csv_generator = setup_csv_generator()

    result = csv_generator.generate_row(line=line)
    assert result == expected_result
