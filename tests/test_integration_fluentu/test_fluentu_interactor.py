from anki_swiss_knife.integration_fluentu.fluentu_interactor import FluentuInteractor


def test__fluentu_interactor__init__should_open_login_page():
    fluentu_interactor = FluentuInteractor()
    assert fluentu_interactor.driver.title == "FluentU"
    assert fluentu_interactor.driver.find_element_by_id("login")
    assert fluentu_interactor.driver.find_element_by_id("password")
