import pytest

from anki_swiss_knife.text_to_speech import TextToSpeech


@pytest.mark.parametrize(
    "csv_path, expected_path",
    [
        (
            "/home/username/anki_swiss_tools/csv/chinese.csv",
            "/home/username/anki_swiss_tools/csv/chinese_with_speech.csv",
        ),
        (
            "C:\\Users\\user\\Desktop\\csv\\chinese.csv",
            "C:\\Users\\user\\Desktop\\csv\\chinese_with_speech.csv",
        ),
    ],
)
def test__text_to_speech__create_csv_with_speech_path__should_return_valid_format(
    csv_path,
    expected_path,
):
    assert TextToSpeech._create_csv_with_speech_path(csv_filepath=csv_path) == expected_path
