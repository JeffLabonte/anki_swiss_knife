from dataclasses import dataclass


@dataclass
class CardWithSpeech:
    word: str
    translation: str = None
    speech: str = None

    def to_list(self):
        return [self.word, f"<div>{self.translation}</div><div>\n{self.speech}<br></div>"]
