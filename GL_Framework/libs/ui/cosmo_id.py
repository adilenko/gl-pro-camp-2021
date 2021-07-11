from libs.ui.page_object.login import LoginPage
from libs.ui.element import Element
from selenium.webdriver.common.by import By
from  libs.ui.page_object.common_elements import CommonElements

class CosmoID():
    user_info_locator = (By.ID, "topbar-user-info-link")
    def __init__(self, driver):
        self.driver = driver
        self.login_pege = LoginPage(self.driver)
        self.common_elements = CommonElements(self.driver)

    def logout(self):
        self.login_pege.open()
        if self.common_elements.logout_btn.is_displayed():
            self.common_elements.logout_btn.click()
        self.login_pege.login_page_url_is_open()


