from libs.ui.browser_provider import BrowserProvider
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from configuration.config import get_config_variable_by_name, ConfigModel
from constants import NAVIGATION_TIMOUT
from urllib import parse
import time



class BasePage:
    def __init__(self, driver, base_url = get_config_variable_by_name(ConfigModel.base_url)):
        self.driver = driver
        self.base_url = base_url


    def go_to(self,url):
        url = self.base_url + url
        self.driver.get(url)

    def wait_for_navigation_to_url(self, expected_url, timout=NAVIGATION_TIMOUT):
        expected_url = parse.urljoin(self.base_url , expected_url)
        current_time = 0
        start_time = time.time()
        while current_time <= start_time + timout:
            if self.driver.current_url == expected_url:
                return True
            time.sleep(0.1)
            current_time = time.time()
        raise TimeoutError(f"Browser can not navigate to {expected_url}")





