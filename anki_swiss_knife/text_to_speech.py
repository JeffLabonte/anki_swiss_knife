import boto3


class TextToSpeech:
    def __init__(
        self,
        language_code: str,
        voice_id: str,
        base_folder_path: str,
    ):
        """
        https://docs.aws.amazon.com/polly/latest/dg/voicelist.html

        Above are the voices and languages that you can select with Polly
        """
        self.language_code = language_code
        self.voice_id = voice_id
        self.base_folder_path = base_folder_path
        self._polly = boto3.client("polly")

    def generate_sound(self, text: str):
        pass

    def _write_audio_file(self, filename: str, content: bytes) -> None:
        audio_path = f"{self.base_folder_path}/{filename}"
        with open(audio_path, "wb") as file:
            file.write(content)
