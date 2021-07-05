from libs.ui.browser_provider import BrowserProvider
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from configuration.config import get_config_variable_by_name, ConfigModel


class BasePage:
    def __init__(self, driver, base_url = get_config_variable_by_name(ConfigModel.base_url)):
        self.driver = driver
        self.base_url = base_url


    def go_to(self,url):
        url = self.base_url + url
        self.driver.get(url)
    #     self.base_url = base_url
    #
    # def click(self, locators, timout=10):
    #     el = self.get_element(locators, EC.element_to_be_clickable)
    #     el.click()
    #
    # def send_text(self, text, *locators, timeout=10):
    #     WebDriverWait(self.driver, timeout).until(
    #         EC.element_to_be_clickable(locators),
    #         message=f"Element by locator {locators} not visible"
    #     )
    #     el = self.get_element(locators, EC.element_to_be_clickable)
    #     el.clear()
    #     # if self.get_attribute("value", locators):
    #     #     self.driver.find_element(locators).send_keys(Keys.CONTROL + "a")
    #     #     self.driver.find_element(locators).send_keys(Keys.DELETE)
    #     el.send_keys(text)
    #
    # def get_text(self, locators, timeout=get_config_variable_by_name(ConfigModel().timeout)):
    #     el = self.get_element(locators)
    #     return el.text()
    #
    # def get_element(self, locators, waiter=EC.visibility_of_element_located,
    #                 timeout=get_config_variable_by_name(ConfigModel().timeout)):
    #     WebDriverWait(self.driver, timeout).until(
    #         waiter(locators),
    #         message=f"Element by locator {locators} not visible"
    #     )
    #     return self.driver.find_element(locators)
