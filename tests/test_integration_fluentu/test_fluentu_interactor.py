from anki_swiss_knife.integration_fluentu.fluentu_interactor import FluentuInteractor


def test__fluentu_interator__init__should_open_login_page():
    fluentu_interactor = FluentuInteractor()
    assert fluentu_interactor.driver.title == "FluentU"
