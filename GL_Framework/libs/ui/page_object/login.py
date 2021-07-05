from selenium.webdriver.common.by import By
from libs.ui.element import Element
from libs.ui.base_app import BasePage


class LoginPage(BasePage):
    login_url = "/login"
    username_fld_locator = (By.ID, "email")
    password_fld_locator = (By.ID, "password")
    login_btn_locator = (By.ID, "signInButton")
    close_annonce_btn_locator = (By.XPATH, "//button[contains(., 'Do not show again')]")

    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.username_fld = Element(self.app, self.username_fld_locator)
        self.password_fld = Element(self.app, self.password_fld_locator)
        self.login_btn = Element(self.app, self.login_btn_locator)
        self.close_annonce_btn = Element(self.app, self.close_annonce_btn_locator)

    def open(self):
        self.go_to(self.login_url)
        if self.close_annonce_btn.is_displayed():
            self.close_annonce_btn.click()


    def login(self, usernae="a", password="b"):
        self.enter_login("username")
        self.enter_password("password")
        self.app.click(locators=self.login_btn)
        # _db_page = DatasetPage(self.app)
        # _db_page.is_loaded()
        # return _db_page

    def enter_login(self, login):
        self.app.send_text(login, self.username_fld)

    def enter_password(self, password):
        self.app.send_text(password, self.username_fld)

    def check_user_loged_in(self):
        return self.app.get_element(self.is_logined) is not None
