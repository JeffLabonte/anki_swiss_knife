import os
from pathlib import Path

import boto3
import progressbar

from anki_swiss_knife.constants import base
from anki_swiss_knife.helper import csv as helper_csv


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
        self.csv_filepath = csv_filepath
        self.csv_with_speech_path = self._create_csv_with_speech_path(csv_filepath=csv_filepath)
        self._polly = boto3.client("polly")
        self._progress_bar = progressbar.ProgressBar(max_value=progressbar.UnknownLength)

    def generate_csv_with_speech(self):
        csv_contents = helper_csv.read_csv(file_path=self.csv_filepath)

        for index, content in enumerate(csv_contents):
            audio_path = self.generate_sound(text=content.word)
            content.speech = f"[sound:{audio_path}]"
            self._progress_bar.update(index)

        helper_csv.write_csv(contents=csv_contents, file_path=self.csv_with_speech_path)

    def generate_sound(self, text: str, anki_user: str = base.DEFAULT_ANKI_USER) -> str:
        response = self._polly.synthesize_speech(
            LanguageCode=self.language_code,
            OutputFormat=self.OUTPUT_FORMAT,
            Text=text,
            VoiceId=self.voice_id,
        )
        csv_folder = Path(self.csv_with_speech_path).parent
        filename = self.csv_with_speech_path.replace(f"{csv_folder}/", "").split(".")[0]
        filename_audio = f"{filename}_{text.replace('/', '')}.{self.OUTPUT_FORMAT}".replace(" ", "_")
        anki_collection_media = os.path.join(Path.home(), base.COLLECTION_MEDIA_LINUX_PATH.format(anki_user=anki_user))
        filename_audio_path = os.path.join(anki_collection_media, filename_audio)

        with open(filename_audio_path, "wb") as file:
            file.write(response["AudioStream"].read())

        return filename_audio

    @staticmethod
    def _create_csv_with_speech_path(csv_filepath) -> str:
        delimiter = "/" if "/" in csv_filepath else "\\"
        filename = csv_filepath.split(delimiter)[-1].split(".")[0]
        new_filename = f"{filename}_with_speech"
        return csv_filepath.replace(filename, new_filename)
