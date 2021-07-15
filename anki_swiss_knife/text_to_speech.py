import boto3


class TextToSpeech:
    OUTPUT_FORMAT = "mp3"

    def __init__(
        self,
        language_code: str,
        voice_id: str,
        csv_filepath: str,
    ):
        """
        https://docs.aws.amazon.com/polly/latest/dg/voicelist.html

        Above are the voices and languages that you can select with Polly
        """
        self.language_code = language_code
        self.voice_id = voice_id
        self.csv_with_speech_path = self._create_csv_with_speech_path(csv_filepath=csv_filepath)
        self._polly = boto3.client("polly")

    def generate_csv_with_speech(self):
        pass

    def generate_sound(self, text: str):
        pass

    def _write_audio_file(self, filename: str, content: bytes) -> None:
        audio_path = f"{self.base_folder_path}/{filename}"
        with open(audio_path, "wb") as file:
            file.write(content)

    @staticmethod
    def _create_csv_with_speech_path(csv_filepath) -> str:
        delimiter = "/" if "/" in csv_filepath else "\\"
        filename = csv_filepath.split(delimiter)[-1].split(".")[0]
        new_filename = f"{filename}_with_speech"
        return csv_filepath.replace(filename, new_filename)
