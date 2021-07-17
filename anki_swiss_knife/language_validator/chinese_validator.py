import re


class ChineseValidator:
    CHINESE_UNICODES = "[\u4e00-\u9FFF]"
    LATIN_UNICODES = "[\u0000-\u007F]"

    NOT_FOUND_RE_SEARCH = 0

    def __init__(self):
        pass

    def _is_character_in_unicode(self, unicode_regex: str, character: str):
        return (
            getattr(
                re.search(
                    unicode_regex,
                    character,
                ),
                "endpos",
                self.NOT_FOUND_RE_SEARCH,
            )
            != self.NOT_FOUND_RE_SEARCH
        )
