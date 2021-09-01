import os

from selenium import webdriver


class FluentuInteractor:
    FLUENTU_LOGIN_URL = "https://www.fluentu.com/login"

    def __init__(self):
        os.environ["MOZ_HEADLESS"] = "1"
        self.driver = webdriver.Firefox()
        self.driver.get(self.FLUENTU_LOGIN_URL)

    def __del__(self):
        self.driver.close()
