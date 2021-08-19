from anki_swiss_knife.language_validator.base_character_validator import BaseCharacterValidator


class ChineseCharacterValidator(BaseCharacterValidator):
    CHINESE_UNICODES = "[\u4e00-\u9FFF]"
    LATIN_UNICODES = "[\u0000-\u007F]"

    # TODO Add extra punctuation in constants
    CHINESE_PONCTUATION = ["？", "！", "。", "，"]

    def is_chinese_character(self, character: str) -> bool:
        return (
            self._is_character_in_unicode_regex(
                unicode_regex=self.CHINESE_UNICODES,
                character=character,
            )
            or character in self.CHINESE_PONCTUATION
        )

    def is_latin_character(self, character: str) -> bool:
        return self._is_character_in_unicode_regex(
            unicode_regex=self.LATIN_UNICODES,
            character=character,
        )

    def has_latin_character_in_line(self, line: str) -> bool:
        return bool(
            [
                character
                for character in line
                if self.is_latin_character(
                    character=character,
                )
            ]
            != []
        )

    def has_chinese_character_in_line(self, line: str) -> bool:
        return bool(
            [
                character
                for character in line
                if self.is_chinese_character(
                    character=character,
                )
            ]
            != []
        )
