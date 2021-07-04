from selenium.webdriver.common.by import By

class LoginPage:

    login_url = "/login"

    username_fld = (By.ID, "email")
    password_fld = (By.id, "password")
    login_btn = (By.ID, "signInButton")
    is_logined = (By.ID, "ttt")

    def __init__(self, app):
        self.app = app

    def open(self):
        self.app.driver.get(self.app.base_url + self.login_url)

    def login(self, usernae, password):
        self.app.enter_login("username")
        self.app.enter_password("password")
        self.app.click(locators=self.login_btn)
        _db_page = DatasetPage(self.app)
        _db_page.is_loaded()
        return _db_page

    def enter_login(self, login):
        pass

    def enter_password(self, password):
        pass

    def check_user_loged_in(self):
        return self.app.get_element(self.is_logined) is not None
