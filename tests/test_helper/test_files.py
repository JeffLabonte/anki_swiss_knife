from collections import namedtuple
from typing import Dict
from unittest.mock import MagicMock, patch

import pytest

from anki_swiss_knife.constants import configs
from anki_swiss_knife.helper.files import create_initial_file, get_parent_from_path

CreateInitialFileMocks = namedtuple(
    "CreateInitialFileMocks",
    ["path_exists_mock", "mocked_function", "mocked_content"],
)

MOCKED_CONTENT = {"a": "mock"}


def setup_create_initial_file(
    file_exists: bool,
    mocked_content: Dict = MOCKED_CONTENT,
    force_create: bool = False,
) -> CreateInitialFileMocks:
    from anki_swiss_knife.helper.files import SUPPORTED_EXTENSIONS

    mocked_function = MagicMock()
    with patch.dict(SUPPORTED_EXTENSIONS, {"ini": mocked_function}), patch(
        "anki_swiss_knife.helper.files.os.path.exists", return_value=file_exists
    ) as exists_mock:
        create_initial_file(
            file_path=configs.CONFIGURATION_FILE_INI,
            content=mocked_content,
            force=force_create,
        )
        return CreateInitialFileMocks(
            path_exists_mock=exists_mock, mocked_function=mocked_function, mocked_content=mocked_content
        )


def test__files__create_initial_file_not_supported__should_raise_not_implemented():
    with pytest.raises(NotImplementedError):
        create_initial_file(
            file_path="/home/jflabonte/.config/test",
            content={"a": "something"},
        )


def test__files_create_initial_file__should_call_function_when_file_doesnt_exists_supported_extension():
    mocks = setup_create_initial_file(file_exists=False)

    mocks.mocked_function.assert_called_once_with(
        file_path=configs.CONFIGURATION_FILE_INI,
        content=mocks.mocked_content,
    )
    mocks.path_exists_mock.assert_called_once_with(
        configs.CONFIGURATION_FILE_INI,
    )


def test__files_create_initial_file__should_not_call_function_when_file_exists():
    mocks = setup_create_initial_file(file_exists=True)

    assert not mocks.mocked_function.called
    mocks.path_exists_mock.assert_called_once_with(configs.CONFIGURATION_FILE_INI)


@pytest.mark.parametrize(
    "file_exists",
    (
        True,
        False,
    ),
)
def test__files_create_inital_file__should_call_function_when_forced(file_exists):
    mocks = setup_create_initial_file(
        file_exists=file_exists,
        force_create=True,
    )

    assert not mocks.path_exists_mock.called
    mocks.mocked_function.called_once_with(
        file_path=configs.CONFIGURATION_FILE_INI,
        content=mocks.mocked_content,
    )


def test__files_get_parent_from_path__should_return_folder_of_file():
    folder = get_parent_from_path(file_path=configs.CONFIGURATION_FILE_INI)
    assert folder == configs.CONFIGURATION_FOLDER
