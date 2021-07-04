from libs.ui.page_object.login import LoginPage
from libs.ui.base_app import BaseApp


class CosmoID(BaseApp):
    def __init__(self, driver):
        super.__init__(driver)
        self.login_pege = LoginPage(self)

    def login(self):
        pass

    def logout(self):
        self