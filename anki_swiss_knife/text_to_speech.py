from pathlib import Path


class TextToSpeech:

    def __init__(self, language_code: str, voice_id: str, base_folder_path: str = Path.home(),):
        self.language_code = language_code
        self.voice_id = voice_id
        self.base_folder_path = base_folder_path

    def generate_sound(self, text: str):
        pass

    def _write_audio_file(self, filename: str, content: bytes) -> None:
        audio_path = f"{self.base_folder_path}/{filename}"
        with open(audio_path, "wb") as file:
            file.write(content)