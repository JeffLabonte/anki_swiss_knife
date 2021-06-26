from anki_swiss_knife.csv_generator import CSVGenerator


def test__csv_generator__is_chinese_character__should_return_true_on_chinese_char():
    csv_generator = CSVGenerator(file_to_convert=None)
    chinese_char = "也"
    assert csv_generator._is_chinese_character(chinese_char) is True


def test__csv_generator__is_chinese_character__should_return_false_on_latin_char():
    csv_generator = CSVGenerator(file_to_convert=None)
    assert csv_generator._is_chinese_character("a") is False
