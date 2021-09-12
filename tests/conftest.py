import os

import pytest

from anki_swiss_knife.constants.configs import CONFIGURATION_FILE_INI


@pytest.fixture
def fake_configs(fs):
    fs.create_file(CONFIGURATION_FILE_INI)
    assert os.path.exists(CONFIGURATION_FILE_INI)
    
    yield fs
