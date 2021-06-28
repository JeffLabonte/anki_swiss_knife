import pytest

from anki_swiss_knife.csv_generator import CSVGenerator


def setup_csv_generator(file_to_convert=None):
    return CSVGenerator(file_to_convert=file_to_convert)


def test__csv_generator__is_chinese_character__should_return_true_on_chinese_char():
    csv_generator = setup_csv_generator()
    chinese_char = "也"
    assert csv_generator._is_chinese_character(chinese_char) is True


def test__csv_generator__is_chinese_character__should_return_false_on_latin_char():
    csv_generator = setup_csv_generator()
    assert csv_generator._is_chinese_character("a") is False


@pytest.mark.parametrize("line, expected_result", [
    ("要 + V. (future tense) will, be going to + V.", "要 + V.;will, be going to + V.",),
    ("放假 fàngjià (v./n.) vacation", "放假;fàngjià (v./n.) vacation")
])
def test__csv_generator__generator_row__should_return_expected_format(
    line,
    expected_result,
):
    csv_generator = setup_csv_generator()

    result = csv_generator.generate_row(line=line)
    assert result == expected_result
