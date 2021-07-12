class DatasetsPage:
    DASHBOARD_URL = '/samples'
    PAGE_LOADED_EL = ""

    def __init__(self,app):
        self.app = app


    def open(self):
        self.app.driver.get(self.app.base_url + self.LOGIN_URL)
        self.app.wait_loaded(self.LOGIN_LOADED_EL)

    def is_loaded(self):
        self.app.wait_loaded(self.PAGE_LOADED_EL)