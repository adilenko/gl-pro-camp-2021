from selenium import webdriver

class Chrome():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.des_cap = webdriver.DesiredCapabilities.CHROME
        self.options.add_argument("--window-maximized")
        # self.options.add_argument("--no-sandbox")
        # self.options.add_argument("--disable-gpu")
        # self.options.add_argument("--window-size=1920.1080")
        self._driver = None


    @property
    def driver(self):
        if self._driver is None:
            self._driver = webdriver.Chrome(options=self.options, desired_capabilities=self.des_cap)
        return self._driver


class BrowserProvider:
    browser = {
       "chrome" : Chrome()
    }

    @staticmethod
    def get_browser(browser_name):
        return BrowserProvider.browser[browser_name].driver