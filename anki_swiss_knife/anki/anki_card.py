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

        second_column = f"{self.pinyin.rstrip()} {following_pinyin.lstrip()}, {self.notes}"
        csv = ";".join([first_column, second_column])
        return f"{csv}\n"
