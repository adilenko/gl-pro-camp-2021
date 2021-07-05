from libs.ui.page_object.login import LoginPage
from libs.ui.element import Element


class CosmoID():
    def __init__(self, driver):
        self.driver = driver
        self.login_pege = LoginPage(self.driver)
