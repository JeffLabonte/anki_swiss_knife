from argparse import ArgumentParser
from unittest.mock import MagicMock, patch

import pytest

from anki_swiss_knife.constants import configs, file_paths
from anki_swiss_knife.main import create_cli_parser, initial_startup


def test__main__create_cli_parser():
    parser = create_cli_parser()
    assert isinstance(parser, ArgumentParser)
    args = parser.parse_args(
        [
            "--gdocs-document-id",
            "something",
            "--text-to-speech",
        ]
    )

    assert args.output_folder == file_paths.DEFAULT_BASE_FOLDER
    assert args.document_id == "something"
    assert args.chinese_not_first is True
    assert args.text_to_speech is True
    assert args.reset_configs is False


@pytest.mark.parametrize(
    "force",
    [
        True,
        False,
    ],
)
def test__main__initial_startup__should_try_to_create(force):
    with patch("anki_swiss_knife.main.files") as files_mock:
        mock = MagicMock()
        files_mock.create_initial_file = mock

        initial_startup(force=force)
        mock.assert_called_once_with(
            file_path=configs.CONFIGURATION_FILE_INI,
            content=configs.DEFAULT_CONFIGURATIONS,
            force=force,
        )
