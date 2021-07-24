import re


class BaseCharacterValidator:

    NOT_FOUND_RE_SEARCH = 0

    def _is_character_in_unicode_regex(self, character: str, unicode_regex: str) -> bool:
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
