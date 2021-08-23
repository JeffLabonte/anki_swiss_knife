from anki_swiss_knife.language_validator.chinese_characters_validator import (
    ChineseCharacterValidator,
)


def test__csv_generator__is_chinese_character__should_return_true_on_chinese_char():
    assert ChineseCharacterValidator().has_chinese_character_in_line("也") is True


def test__csv_generator__is_chinese_character__should_return_false_on_latin_char():
    assert ChineseCharacterValidator().has_chinese_character_in_line("a") is False
