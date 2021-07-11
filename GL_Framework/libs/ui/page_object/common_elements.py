from selenium.webdriver.common.by import By
from libs.ui.element import Element
from libs.ui.base_app import BasePage
from configuration.config import ConfigModel, get_config_variable_by_name


class CommonElements:
    logout_btn_locator = (By.ID, "topbar-logout-button")
    def __init__(self, app):
        self.app = app
        self.logout_btn= Element(self.app, self.logout_btn_locator)



