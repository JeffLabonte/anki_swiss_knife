from anki_swiss_knife.language_validator.base_character_validator import BaseCharacterValidator


class ChineseCharacterValidator(BaseCharacterValidator):
    CHINESE_UNICODES = "[\u4e00-\u9FFF]"
    LATIN_UNICODES = "[\u0000-\u007F]"

    def is_chinese_character(self, character: str) -> bool:
        return self._is_character_in_unicode_regex(
            unicode_regex=self.CHINESE_UNICODES,
            character=character,
        )

    def is_latin_character(self, character: str) -> bool:
        return self._is_character_in_unicode_regex(
            unicode_regex=self.LATIN_UNICODES,
            character=character,
        )
