from dataclasses import dataclass


@dataclass
class CardWithSpeech:
    word: str
    translation: str = None
    speech: str = None

    def to_list(self):
        return [
            self.word,
            f"{self.translation}\n{self.speech}",
        ]
