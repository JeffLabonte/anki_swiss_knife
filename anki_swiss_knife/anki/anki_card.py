from dataclasses import dataclass


@dataclass
class ChineseAnkiCard:
    chinese_character: str
    pinyin: str
    translation: str
    notes: str

    def to_csv(self, is_chinese_first: bool) -> str:
        first_column = self.chinese_character if is_chinese_first else self.translation
        following_pinyin = self.translation if is_chinese_first else self.chinese_character

        second_column = f"{self.pinyin.rstrip()}\n{following_pinyin.lstrip()}"
        csv = ";".join([first_column, second_column, self.notes])
        return f"{csv}\n"
