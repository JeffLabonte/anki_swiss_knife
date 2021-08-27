import argparse

from anki_swiss_knife.constants import file_paths
from anki_swiss_knife.main import create_cli_parser


def test__main__create_cli_parser():
    parser = create_cli_parser()
    assert isinstance(parser, argparse.ArgumentParser)
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
