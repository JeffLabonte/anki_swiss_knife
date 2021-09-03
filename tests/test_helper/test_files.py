import pytest

from anki_swiss_knife.helper.files import create_initial_file
from anki_swiss_knife.constants import base


def test__files__create_file_not_supported__should_raise_not_implemented():
    with pytest.raises(NotImplementedError):
        create_initial_file(
            file_path="/home/jflabonte/.config/test",
            content={"a": "something"},
        )


def test__files__create_init_file__should_not_raise_with__valid_format():
    create_initial_file(
        file_path=base.CONFIGURATION_FILE_INI,
        content={"a": "dev"},
    )
