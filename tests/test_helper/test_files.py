from unittest.mock import MagicMock, patch

import pytest

from anki_swiss_knife.constants import base
from anki_swiss_knife.helper.files import create_initial_file


def test__files__create_initial_file_not_supported__should_raise_not_implemented():
    with pytest.raises(NotImplementedError):
        create_initial_file(
            file_path="/home/jflabonte/.config/test",
            content={"a": "something"},
        )


def test__files__create_initial_file__should_not_raise_with__valid_format():
    create_initial_file(
        file_path=base.CONFIGURATION_FILE_INI,
        content={"a": "dev"},
    )


def test__files_create_initial_file__should_call_when_file_doesnt_exists_supported_extension():
    from anki_swiss_knife.helper.files import SUPPORTED_EXTENSIONS

    mocked_function = MagicMock()
    with patch.dict(SUPPORTED_EXTENSIONS, {"ini": mocked_function}), patch(
        "anki_swiss_knife.helper.files.os.path.exists", return_value=False
    ) as exists_mock:
        create_initial_file(
            file_path=base.CONFIGURATION_FILE_INI,
            content={"a": "dev"},
        )
        assert mocked_function.called
        assert exists_mock.called

        mocked_function.assert_called_once_with(
            file_path=base.CONFIGURATION_FILE_INI,
            content={"a": "dev"},
        )
        exists_mock.assert_called_once_with(base.CONFIGURATION_FILE_INI)
