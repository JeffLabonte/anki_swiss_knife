from anki_swiss_knife.constants import configs as configs_constant
from anki_swiss_knife.helper import configs as configs_helper


def test__helper_configs__read_configs__should_return_dict_with_configs(fake_configs):
    config_dict = configs_helper.read_config(file_path=configs_constant.CONFIGURATION_FILE_INI)

    assert isinstance(config_dict, dict)

    for section, configs in configs_constant.DEFAULT_CONFIGURATIONS.items():
        config_section = config_dict.pop(section)
        for config, value in configs.items():
            if config_section:
                assert config_section.pop(config, False) == value, f"Value for config: {config} doesn't match"

    assert not config_dict
