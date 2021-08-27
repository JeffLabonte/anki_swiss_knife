from unittest.mock import mock_open, patch

import pytest

from anki_swiss_knife.helper import csv


def test__helper_csv__read_file__should_fail_if_path_not_csv_extension():
    with pytest.raises(RuntimeError):
        csv.read_csv(file_path="file.txt")


def test__helper_csv__read_csv__should_return_card_with_speech():
    with patch("builtins.open", mock_open(read_data="chinese;notes")) as open_read:
        extracted_data = csv.read_csv(file_path="file.csv")
        assert open_read.called
        assert len(extracted_data) == 1
        assert extracted_data[0].word == "chinese"
