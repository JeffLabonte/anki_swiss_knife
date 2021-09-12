import os

import pytest

from anki_swiss_knife.constants.configs import CONFIGURATION_FILE_INI
from anki_swiss_knife.main import initial_startup


@pytest.fixture
def fake_configs(fs):
    fs.create_file(CONFIGURATION_FILE_INI)
    initial_startup()
    yield fs
