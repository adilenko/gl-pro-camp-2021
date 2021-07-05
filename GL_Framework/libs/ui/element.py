from selenium.common.exceptions import (NoSuchElementException, ElementNotVisibleException,
                                        ElementNotSelectableException, StaleElementReferenceException, TimeoutException,
                                        ElementClickInterceptedException, MoveTargetOutOfBoundsException)
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import constants
from configuration.config import ConfigModel, get_config_variable_by_name
from libs.ui.base_app import BasePage

class Element():
    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = tuple(locator[:2])

    @property
    def text(self):
        return self.find_element().text


    def find_element(self, timeout=get_config_variable_by_name(ConfigModel().timeout)):
        return self._wait(timeout=timeout).until(EC.presence_of_element_located(self.locator))


    def find_elements(self, locator):
        return self.find_element().find_elements(*locator[:2])

    def click(self, wait_to_be_clickable=True):
        if wait_to_be_clickable:
            self.wait_for_clickable()
        self.find_element().click()

    def send_keys(self, text):
        self.wait_for_clickable()
        element = self.find_element()
        element.clear()
        element.send_keys(text)

    def wait_for_visible(self, timeout=get_config_variable_by_name(ConfigModel().timeout)):
        element = self._wait(timeout).until(EC.visibility_of_any_elements_located(self.locator))
        return element

    def wait_for_clickable(self, timeout=get_config_variable_by_name(ConfigModel().timeout)):
        element = self._wait(timeout).until(EC.element_to_be_clickable(self.locator))
        return element

    def _wait(self, timeout=get_config_variable_by_name(ConfigModel().timeout)):
        wait = WebDriverWait(driver=self.driver, timeout=timeout, ignored_exceptions=(
            NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException,
            StaleElementReferenceException, ElementClickInterceptedException))
        return wait

    def is_displayed(self, timeout=get_config_variable_by_name(ConfigModel().timeout)):
        try:
            element = self.find_element(timeout=timeout)
            return element.is_displayed()
        except TimeoutException:
            return False