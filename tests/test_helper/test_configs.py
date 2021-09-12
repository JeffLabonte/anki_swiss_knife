from anki_swiss_knife.constants import configs as configs_constant
from anki_swiss_knife.helper import configs


def test__helper_configs__read_configs__should_return_dict_with_configs(fake_configs):
    config_dict = configs.read_config(file_path=configs_constant.CONFIGURATION_FILE_INI)

    assert isinstance(config_dict, dict)
